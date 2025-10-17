from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
from typing import List
from backend.app.db import get_session
from backend.app.models import Post
from backend.app.schemas.post import PostResponse, PostCreate, PostUpdate
from fastapi.responses import HTMLResponse
import bleach
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[PostResponse])
def list_posts(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    post_type: str = Query(None),
    status: str = Query(None),
    session: Session = Depends(get_session)
):
    """List all posts with optional filtering."""
    statement = select(Post).offset(skip).limit(limit)

    if post_type:
        statement = statement.where(Post.post_type == post_type)
    if status:
        statement = statement.where(Post.status == status)

    posts = session.exec(statement).all()
    return posts


@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int, session: Session = Depends(get_session)):
    """Get a single post by ID."""
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/slug/{slug}", response_model=PostResponse)
def get_post_by_slug(slug: str, session: Session = Depends(get_session)):
    """Get a single post by slug."""
    statement = select(Post).where(Post.slug == slug)
    post = session.exec(statement).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostResponse, status_code=201)
def create_post(post: PostCreate, session: Session = Depends(get_session)):
    """Create a new post."""
    # Check if slug already exists
    existing = session.exec(select(Post).where(Post.slug == post.slug)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Slug already exists")

    db_post = Post(**post.model_dump())
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.patch("/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post_update: PostUpdate,
    session: Session = Depends(get_session)
):
    """Update a post."""
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    update_data = post_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post, key, value)

    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, session: Session = Depends(get_session)):
    """Delete a post."""
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    session.delete(db_post)
    session.commit()
    return None


# --- sanitización segura para contenido HTML de posts (mejorada) ---
ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS) | {
    "img", "figure", "figcaption", "details", "summary",
    "table", "thead", "tbody", "tr", "th", "td", "caption",
    "pre", "code", "meter", "progress", "blockquote", "caption"
}

ALLOWED_ATTRIBUTES = {
    **bleach.sanitizer.ALLOWED_ATTRIBUTES,
    "img": ["src", "alt", "width", "height", "loading"],
    "a": ["href", "title", "target", "rel"],
    "*": ["class", "id"]
}

# Protocols: esquemas válidos. No incluir "/" (no es necesario para rutas relativas).
ALLOWED_PROTOCOLS = ["http", "https", "mailto", "tel"]


def sanitize_post_html(html: str) -> str:
    """
    Limpia y normaliza HTML de posts para reducir riesgo XSS.
    strip=True elimina etiquetas no permitidas.
    En caso de error devuelve una cadena vacía segura.
    """
    try:
        cleaned = bleach.clean(
            html or "",
            tags=list(ALLOWED_TAGS),
            attributes=ALLOWED_ATTRIBUTES,
            protocols=ALLOWED_PROTOCOLS,
            strip=True
        )
        return cleaned
    except Exception:
        logger.exception("Error sanitizando HTML del post; devolviendo contenido vacío.")
        return ""


# Cabecera CSP por defecto (ajústala según tus necesidades)
DEFAULT_CSP = (
    "default-src 'self'; "
    "img-src 'self' data: https:; "
    "style-src 'self' 'unsafe-inline'; "
    "font-src 'self' https:; "
    "script-src 'none'; "
    "frame-ancestors 'none';"
)


@router.get("/{post_id}/render", response_class=HTMLResponse)
def render_post(post_id: int, session: Session = Depends(get_session)):
    """
    Devuelve el campo `content` del post COMO HTML (Content-Type: text/html).
    La salida se sanitiza para mitigar XSS y se devuelve con una CSP básica.
    """
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    safe_html = sanitize_post_html(post.content)

    # Auditoría ligera: detectar sanitizaciones agresivas
    if post.content and len(safe_html) < (len(post.content) // 2):
        logger.info("Sanitización intensa: contenido reducido para post_id=%s", post_id)

    headers = {
        "Content-Security-Policy": DEFAULT_CSP,
        "X-Frame-Options": "DENY",
    }

    return HTMLResponse(content=safe_html, status_code=200, headers=headers)
