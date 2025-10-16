# Admin Panel Documentation

## Overview

The admin panel provides a web-based interface for managing content and customizing the visual design of your ecommerce site.

**Access**: http://localhost:5173/admin

## Features

### 1. Posts & Content Management

Create and manage various types of content for your site:

- **Posts** - Blog posts, articles, news
- **Pages** - Static pages (About, Terms, etc.)
- **Banners** - Homepage banners, promotional content

#### Creating a Post

1. Navigate to Admin Panel → "Posts & Content" tab
2. Click "New Post"
3. Fill in the form:
   - **Title**: Post title (auto-generates slug)
   - **Slug**: URL-friendly identifier (e.g., `my-first-post`)
   - **Content**: HTML content (supports full HTML)
   - **Excerpt**: Brief summary
   - **Type**: post, page, or banner
   - **Status**: draft or published
   - **Published**: Toggle visibility
4. Click "Create Post"

#### Editing a Post

1. Find the post in the list
2. Click "Edit"
3. Make changes
4. Click "Update Post"

#### Post Types

- **post**: Regular blog posts/articles
- **page**: Static pages (About, Contact, etc.)
- **banner**: Homepage banners or promotional content

### 2. Visual Design Editor

Customize the look and feel of your site in real-time:

#### Color Customization

Edit the main color palette:
- **Primary**: Main brand color (buttons, links)
- **Secondary**: Accent color
- **Background**: Page background
- **Text**: Default text color
- **Accent**: Highlights and special elements

#### Typography

Customize fonts:
- **Heading Font**: Font for titles and headings
- **Body Font**: Font for regular text

Available fonts:
- Inter
- Roboto
- Open Sans
- Poppins
- Montserrat
- Lato
- Source Sans Pro

#### Layout Options

- **Border Radius**: Control roundness of corners (none, sm, md, lg, xl)
- **Spacing**: Adjust element spacing (compact, normal, relaxed)

#### Live Preview

The design editor includes a real-time preview showing:
- Sample heading with your chosen fonts and colors
- Body text example
- Button styles
- Card components
- Color palette display

Changes are reflected immediately in the preview panel.

#### Saving Your Design

1. Make your color, typography, and layout changes
2. Use the live preview to see results
3. Click "Save Design"
4. Design is applied site-wide

## API Endpoints

### Posts API

**Base URL**: `/api/v1/posts/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/posts/` | List all posts |
| GET | `/api/v1/posts/{id}` | Get post by ID |
| GET | `/api/v1/posts/slug/{slug}` | Get post by slug |
| POST | `/api/v1/posts/` | Create new post |
| PATCH | `/api/v1/posts/{id}` | Update post |
| DELETE | `/api/v1/posts/{id}` | Delete post |

**Query Parameters** (GET list):
- `skip`: Number of posts to skip (pagination)
- `limit`: Maximum posts to return
- `post_type`: Filter by type (post, page, banner)
- `status`: Filter by status (draft, published)

**Example POST Request**:
```json
{
  "title": "Welcome to Our Store",
  "slug": "welcome-to-our-store",
  "content": "<h2>Hello!</h2><p>Welcome to our new store.</p>",
  "excerpt": "A brief introduction to our store",
  "status": "published",
  "post_type": "post",
  "is_published": true
}
```

### Design API

**Base URL**: `/api/v1/design/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/design/` | List all designs |
| GET | `/api/v1/design/active` | Get active design |
| POST | `/api/v1/design/` | Create design |
| PATCH | `/api/v1/design/{id}` | Update design |
| DELETE | `/api/v1/design/{id}` | Delete design |

**Example Design Structure**:
```json
{
  "name": "Custom Theme",
  "colors": {
    "primary": "#3B82F6",
    "secondary": "#10B981",
    "background": "#FFFFFF",
    "text": "#1F2937",
    "accent": "#F59E0B"
  },
  "typography": {
    "heading_font": "Poppins",
    "body_font": "Inter"
  },
  "layout": {
    "border_radius": "lg",
    "spacing": "relaxed"
  },
  "components": {}
}
```

## Database Models

### Post Model

```python
class Post:
    id: int
    title: str
    slug: str (unique)
    content: str (HTML)
    excerpt: str (optional)
    featured_image: str (optional)
    status: str (draft/published)
    post_type: str (post/page/banner)
    author_id: int (optional)
    is_published: bool
    created_at: datetime
    updated_at: datetime
```

### SiteDesign Model

```python
class SiteDesign:
    id: int
    name: str (unique)
    is_active: bool
    colors: dict (JSON)
    typography: dict (JSON)
    layout: dict (JSON)
    components: dict (JSON)
    created_at: datetime
    updated_at: datetime
```

## Usage Tips

### Content Management

1. **Draft First**: Create posts as drafts to preview before publishing
2. **SEO-Friendly Slugs**: Use descriptive, lowercase slugs with hyphens
3. **HTML Content**: You can use full HTML in the content field for rich formatting
4. **Types**: Use different post types to organize content:
   - `post` for blog content
   - `page` for static pages
   - `banner` for promotional content

### Design Customization

1. **Start with Colors**: Define your brand colors first
2. **Preview Often**: Use the live preview to see changes immediately
3. **Consistency**: Keep font pairings simple (1-2 fonts max)
4. **Contrast**: Ensure text color has good contrast with background
5. **Save Regularly**: Save your design to persist changes

### Best Practices

- **Backup Content**: Export important posts before major changes
- **Test Designs**: Preview designs before activating site-wide
- **Mobile-Friendly**: Consider how colors and fonts appear on mobile
- **Performance**: Minimize use of custom fonts for better load times

## Future Enhancements

Planned features for the admin panel:

- [ ] Rich text WYSIWYG editor (replace HTML textarea)
- [ ] Media library for image uploads
- [ ] User authentication and roles
- [ ] Post categories and tags
- [ ] SEO meta fields
- [ ] Scheduled publishing
- [ ] Revision history
- [ ] Bulk actions
- [ ] Export/import content
- [ ] Custom CSS injection
- [ ] Mobile responsive preview
- [ ] A/B testing for designs

## Troubleshooting

**Posts not appearing?**
- Check `is_published` is set to true
- Verify `status` is "published"
- Clear browser cache

**Design changes not saving?**
- Check browser console for errors
- Verify backend is running
- Check API endpoint connectivity

**Slug already exists error?**
- Slugs must be unique
- Try a different slug or edit the existing post

## Support

For issues or questions:
- Check API documentation at http://localhost:8000/docs
- Review browser console for errors
- Verify backend logs for API errors
