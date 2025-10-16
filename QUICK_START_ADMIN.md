# Quick Start Guide - Admin Panel

## Issue Fixed!

The white screen issue has been resolved. The problem was that the vite.config.js needed the package.json to specify `"type": "module"` for ESM imports.

## Current Status

✅ **Frontend Running**: http://localhost:5174
✅ **Backend Running**: http://localhost:8000
✅ **Admin Panel**: http://localhost:5174/admin

**Note**: Port changed to 5174 because 5173 was in use.

## How to Access Admin Panel

### Option 1: Direct URL
Open your browser and navigate to:
```
http://localhost:5174/admin
```

### Option 2: From Homepage
1. Go to http://localhost:5174
2. Click "Admin" in the navigation bar (purple link in the top right)

## What You Can Do

### 1. Manage Posts & Content
- Click "Posts & Content" tab
- Create posts, pages, or banners
- Edit existing content
- Delete unwanted posts

### 2. Customize Visual Design
- Click "Visual Design" tab
- Pick colors with color pickers
- Choose fonts from dropdowns
- Adjust layout settings
- See live preview of changes
- Click "Save Design" to apply

## Testing the Admin Panel

### Create Your First Post

1. Navigate to http://localhost:5174/admin
2. You should see "Posts & Content" tab active
3. Click "+ New Post" button
4. Fill in:
   - **Title**: "Welcome to My Store"
   - **Slug**: Auto-generates as "welcome-to-my-store"
   - **Content**: `<h2>Hello!</h2><p>This is my first post.</p>`
   - **Type**: Keep as "post"
   - **Status**: "published"
   - **Published**: Check the box
5. Click "Create Post"
6. You should see your post in the list!

### Customize Your Design

1. Click "Visual Design" tab
2. Try changing colors:
   - Click any color picker
   - Choose a new color
   - See it update in the preview
3. Change fonts:
   - Select "Poppins" for heading font
   - See preview update
4. Click "Save Design"

## API Testing

### Test Posts API
```bash
# List all posts
curl http://localhost:8000/api/v1/posts/

# Create a post
curl -X POST http://localhost:8000/api/v1/posts/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Post",
    "slug": "test-post",
    "content": "<p>Test content</p>",
    "status": "published",
    "post_type": "post",
    "is_published": true
  }'
```

### Test Design API
```bash
# Get active design
curl http://localhost:8000/api/v1/design/active
```

## Troubleshooting

### White Screen?
1. Check browser console (F12) for errors
2. Verify both servers are running:
   - Frontend: http://localhost:5174
   - Backend: http://localhost:8000
3. Try refreshing the page (Ctrl+R or F5)
4. Clear browser cache (Ctrl+Shift+Delete)

### Can't Save Posts?
- Check backend is running
- Open browser console to see error messages
- Verify slug is unique (no duplicate slugs allowed)

### Design Changes Not Saving?
- Check backend console for errors
- Verify CORS is enabled (already done)
- Try creating a new design instead of updating

## Next Steps

1. **Try the Admin Panel**: http://localhost:5174/admin
2. **Create Content**: Add some posts and pages
3. **Customize Design**: Make it your own with colors and fonts
4. **View API Docs**: http://localhost:8000/docs (Swagger)

## Full Documentation

- **[ADMIN_PANEL.md](ADMIN_PANEL.md)** - Complete admin panel guide
- **[README.md](README.md)** - Project overview
- **[SETUP.md](SETUP.md)** - Setup instructions

## Important Notes

### Windows 10 Compatibility
- ✅ All features tested on Windows 10
- ✅ Scripts compatible with Windows (`.bat`) and Linux (`.sh`)
- ✅ Database uses SQLite (no additional setup needed)

### Port Information
- Frontend was moved to **port 5174** (from 5173)
- If you need port 5173, stop other Vite instances first
- Backend remains on port 8000

## Summary

Your admin panel is ready! Access it at:

**http://localhost:5174/admin**

Start by creating your first post or customizing the design colors. All changes are saved to the database and persist across restarts.

Enjoy building your ecommerce site! 🚀
