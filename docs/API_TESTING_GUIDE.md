# API Testing Guide - CMS Endpoints

Quick reference for testing the new CMS API endpoints.

## Prerequisites

1. Start the backend server:
```bash
start-backend.bat
```

2. Verify it's running:
```
http://localhost:8000/docs
```

---

## Testing Workflow

### 1. Create a Hero Section

**Request:**
```http
POST http://localhost:8000/api/v1/sections/
Content-Type: application/json

{
  "page": "home",
  "section_type": "hero",
  "order": 0,
  "is_active": true,
  "content": {
    "headline": "Welcome to Our Store",
    "subheadline": "Discover amazing products at great prices",
    "background_image_url": null,
    "cta_text": "Shop Now",
    "cta_url": "/catalog"
  }
}
```

**Expected Response:** `201 Created`
```json
{
  "id": 1,
  "page": "home",
  "section_type": "hero",
  "order": 0,
  "is_active": true,
  "content": { ... },
  "created_at": "2025-10-16T...",
  "updated_at": "2025-10-16T..."
}
```

---

### 2. Upload an Image

**Using Swagger UI:**
1. Go to `http://localhost:8000/docs`
2. Find `POST /api/v1/assets/upload`
3. Click "Try it out"
4. Upload a JPG/PNG file (< 10MB)
5. Optionally add alt_text
6. Click "Execute"

**Expected Response:** `201 Created`
```json
{
  "id": 1,
  "filename": "my-image.jpg",
  "file_path": "uploads/2025/10/550e8400-e29b-41d4-a716-446655440000.jpg",
  "file_type": "image",
  "mime_type": "image/jpeg",
  "file_size": 245760,
  "alt_text": "Hero banner",
  "url": "/static/uploads/2025/10/550e8400-e29b-41d4-a716-446655440000.jpg",
  "created_at": "2025-10-16T..."
}
```

**Access the uploaded image:**
```
http://localhost:8000/static/uploads/2025/10/550e8400-e29b-41d4-a716-446655440000.jpg
```

---

### 3. Update Hero with Uploaded Image

**Request:**
```http
PUT http://localhost:8000/api/v1/sections/1
Content-Type: application/json

{
  "page": "home",
  "section_type": "hero",
  "order": 0,
  "is_active": true,
  "content": {
    "headline": "Welcome to Our Store",
    "subheadline": "Discover amazing products at great prices",
    "background_image_url": "/static/uploads/2025/10/550e8400-e29b-41d4-a716-446655440000.jpg",
    "cta_text": "Shop Now",
    "cta_url": "/catalog"
  }
}
```

---

### 4. Create Menu Items

**Home:**
```http
POST http://localhost:8000/api/v1/menu-items/
Content-Type: application/json

{
  "label": "Home",
  "url": "/",
  "order": 0,
  "is_active": true,
  "opens_new_tab": false
}
```

**Shop:**
```http
POST http://localhost:8000/api/v1/menu-items/
Content-Type: application/json

{
  "label": "Shop",
  "url": "/catalog",
  "order": 1,
  "is_active": true,
  "opens_new_tab": false
}
```

**About:**
```http
POST http://localhost:8000/api/v1/menu-items/
Content-Type: application/json

{
  "label": "About",
  "url": "/about",
  "order": 2,
  "is_active": true,
  "opens_new_tab": false
}
```

---

### 5. Create a Content Block

**Request:**
```http
POST http://localhost:8000/api/v1/sections/
Content-Type: application/json

{
  "page": "home",
  "section_type": "content_block",
  "order": 1,
  "is_active": true,
  "content": {
    "title": "Why Shop With Us",
    "body": "We offer the best selection of quality products at competitive prices. Our customer service team is ready to help you 24/7.",
    "image_url": null,
    "image_position": "right"
  }
}
```

---

### 6. Create a Product Grid

**Request:**
```http
POST http://localhost:8000/api/v1/sections/
Content-Type: application/json

{
  "page": "home",
  "section_type": "product_grid",
  "order": 2,
  "is_active": true,
  "content": {
    "title": "Featured Products",
    "product_ids": [1, 2, 3, 4, 5, 6],
    "layout": "grid",
    "columns": 3,
    "show_add_to_cart": true
  }
}
```

---

### 7. List All Sections for Homepage

**Request:**
```http
GET http://localhost:8000/api/v1/sections/?page=home
```

**Expected Response:**
```json
{
  "sections": [
    {
      "id": 1,
      "page": "home",
      "section_type": "hero",
      "order": 0,
      ...
    },
    {
      "id": 2,
      "page": "home",
      "section_type": "content_block",
      "order": 1,
      ...
    },
    {
      "id": 3,
      "page": "home",
      "section_type": "product_grid",
      "order": 2,
      ...
    }
  ],
  "count": 3
}
```

---

### 8. Reorder Sections

Move product grid to position 1 (above content block):

**Request:**
```http
PATCH http://localhost:8000/api/v1/sections/3/reorder?new_order=1
```

**Expected Result:**
- Hero: order 0
- Product Grid: order 1 (moved up)
- Content Block: order 1 (will need manual adjustment)

---

## Testing Invalid Content

### Test 1: Invalid Section Type

```http
POST http://localhost:8000/api/v1/sections/
Content-Type: application/json

{
  "page": "home",
  "section_type": "hero",
  "order": 0,
  "is_active": true,
  "content": {
    "invalid_field": "this won't validate"
  }
}
```

**Expected:** `422 Unprocessable Entity` - Content validation failed

---

### Test 2: Too Many Products

```http
POST http://localhost:8000/api/v1/sections/
Content-Type: application/json

{
  "page": "home",
  "section_type": "product_grid",
  "order": 0,
  "is_active": true,
  "content": {
    "title": "All Products",
    "product_ids": [1, 2, 3, ... 100],
    "layout": "grid",
    "columns": 3
  }
}
```

**Expected:** `422 Unprocessable Entity` - Maximum 50 products per grid

---

### Test 3: Large File Upload

Try uploading a file > 10MB:

**Expected:** `413 Payload Too Large` - File too large

---

### Test 4: Invalid File Type

Try uploading a .exe or .pdf file:

**Expected:** `415 Unsupported Media Type` - Unsupported file type

---

## PowerShell Testing Examples

### Create Hero Section
```powershell
$body = @{
    page = "home"
    section_type = "hero"
    order = 0
    is_active = $true
    content = @{
        headline = "Welcome"
        subheadline = "Shop now"
        cta_text = "Browse"
        cta_url = "/catalog"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sections/" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

### List Sections
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/sections/?page=home"
```

### Create Menu Item
```powershell
$body = @{
    label = "Home"
    url = "/"
    order = 0
    is_active = $true
    opens_new_tab = $false
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/menu-items/" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

---

## Verification Checklist

After creating content, verify:

- [x] Sections appear in correct order
- [x] Images are accessible at their URLs
- [x] Menu items are ordered correctly
- [x] Content validation catches errors
- [x] File upload creates dated directories
- [x] Reorder endpoint updates order field

---

## Next Steps

Once backend testing is complete:

1. **Day 2**: Create frontend admin components
   - ContentManager.jsx - list/edit sections
   - AssetManager.jsx - upload/browse images
   - MenuManager.jsx - edit navigation

2. **Day 3**: Integrate with homepage
   - Fetch sections from API
   - Render dynamically
   - Use menu items in NavBar

3. **Day 4**: Polish UX
   - Loading states
   - Error handling
   - Confirm dialogs

4. **Day 5**: Final testing
   - End-to-end workflows
   - Documentation updates
   - Demo recording

---

**Swagger UI:** http://localhost:8000/docs (Interactive testing)
**ReDoc:** http://localhost:8000/redoc (API documentation)
**Database:** `backend/ecommerce.db` (SQLite file)
**Uploads:** `backend/static/uploads/` (Check after upload)
