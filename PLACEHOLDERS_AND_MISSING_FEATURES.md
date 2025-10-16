# Placeholders and Missing Features

**Date**: October 16, 2025
**Status**: Development Phase

---

## 🔍 Identified Placeholders in Code

### 1. **Shopping Cart (Non-Functional)**

**Location**: `frontend/src/components/NavBar.jsx:28` and `:74`

**Current State**:
```jsx
<button className="...">Carrito (0)</button>
```

**Issue**: Button displays "Carrito (0)" but has no functionality
- No click handler
- No cart state management
- No cart icon/badge
- No cart modal or page

**Required Implementation**:
- [ ] Cart context provider (useState/reducer)
- [ ] Add to cart functionality
- [ ] Cart dropdown/modal
- [ ] Cart page with item list
- [ ] Quantity adjustment
- [ ] Remove from cart
- [ ] Local storage persistence
- [ ] Cart total calculation

---

### 2. **Catalog Page (Coming Soon)**

**Location**: `frontend/src/App.jsx:18`

**Current State**:
```jsx
<h2>Catálogo (próximamente)</h2>
```

**Issue**: Catalog route exists but shows "Coming Soon" message

**Required Implementation**:
- [ ] Product filtering (by category, price, etc.)
- [ ] Product sorting (price, name, date)
- [ ] Search functionality
- [ ] Pagination or infinite scroll
- [ ] Category navigation
- [ ] Filter sidebar

---

### 3. **Sample Content in DesignEditor**

**Location**: `frontend/src/components/admin/DesignEditor.jsx`

**Current State**: Uses generic "Sample Heading", "Sample Card", "Sample Button" text

**Issue**: Preview panel shows generic sample content instead of actual site components

**Suggested Improvement**:
- [ ] Show actual ProductCard preview
- [ ] Show actual NavBar preview
- [ ] Show actual Button components
- [ ] Make preview interactive

---

### 4. **Product Images from Placeholder Script**

**Location**: `backend/backend/static/placeholders/`

**Current State**: Products use generated placeholder images from `gen_placeholders.py`

**Issue**:
- Images are generated programmatically with Pillow
- Not real product images
- Path: `/static/placeholders/sample.png`

**Required Implementation**:
- [ ] Image upload functionality
- [ ] Image storage (S3, Cloudinary, or local)
- [ ] Image resizing/optimization
- [ ] Multiple images per product
- [ ] Image gallery component

---

## 🚫 Missing Core Features

### 5. **User Authentication**

**Status**: ❌ NOT IMPLEMENTED

**Missing**:
- [ ] User registration
- [ ] Login/logout
- [ ] Password hashing (bcrypt)
- [ ] JWT token generation
- [ ] Token refresh mechanism
- [ ] Protected routes (admin panel)
- [ ] User session management
- [ ] "Remember me" functionality
- [ ] Password reset flow

**Security Risk**: Admin panel is completely public!

---

### 6. **Product Detail Page**

**Status**: ❌ NOT IMPLEMENTED

**Current**: Clicking a product card does nothing

**Required**:
- [ ] Product detail route (`/product/:slug`)
- [ ] Product detail component
- [ ] Image gallery/carousel
- [ ] Add to cart button
- [ ] Product description rendering (HTML)
- [ ] Related products section
- [ ] Breadcrumb navigation
- [ ] Share buttons
- [ ] Product reviews (future)

---

### 7. **Checkout Flow**

**Status**: ❌ NOT IMPLEMENTED

**Required**:
- [ ] Checkout page
- [ ] Shipping address form
- [ ] Payment method selection
- [ ] Order summary
- [ ] Stripe integration (payment processing)
- [ ] Order confirmation page
- [ ] Email confirmation
- [ ] Order history (user account)

---

### 8. **Order Management**

**Status**: ❌ NOT IMPLEMENTED

**Database**: No Order model exists

**Required**:
- [ ] Order model (backend)
- [ ] Order API endpoints
- [ ] Admin order management UI
- [ ] Order status tracking
- [ ] Order search/filter
- [ ] Export orders (CSV/Excel)

---

### 9. **Image Upload for Posts**

**Status**: ❌ NOT IMPLEMENTED

**Current**: PostManager has `featured_image` field but no upload mechanism

**Required**:
- [ ] File upload endpoint (backend)
- [ ] File upload component (frontend)
- [ ] Image preview before upload
- [ ] Image validation (size, format)
- [ ] Featured image display in post list
- [ ] Image storage solution

---

### 10. **Category/Tag System**

**Status**: ❌ NOT IMPLEMENTED

**Missing**:
- [ ] Category model
- [ ] Product-category relationship
- [ ] Tag model (optional)
- [ ] Category CRUD in admin
- [ ] Category navigation in frontend
- [ ] Category filtering

---

### 11. **Search Functionality**

**Status**: ❌ NOT IMPLEMENTED

**Required**:
- [ ] Search API endpoint (full-text search)
- [ ] Search bar component
- [ ] Search results page
- [ ] Search suggestions/autocomplete
- [ ] Search history

---

### 12. **Email System**

**Status**: ❌ NOT IMPLEMENTED

**Required**:
- [ ] Email service setup (SMTP, SendGrid, etc.)
- [ ] Order confirmation emails
- [ ] Password reset emails
- [ ] Welcome emails
- [ ] Newsletter subscription
- [ ] Email templates

---

### 13. **User Dashboard**

**Status**: ❌ NOT IMPLEMENTED

**Required**:
- [ ] User account page
- [ ] Order history
- [ ] Saved addresses
- [ ] Wishlist
- [ ] Account settings
- [ ] Profile editing

---

### 14. **Inventory Management**

**Status**: ⚠️ PARTIAL (stock field exists but not used)

**Current**: Product model has `stock` field but no management

**Required**:
- [ ] Stock tracking
- [ ] Low stock alerts
- [ ] Out of stock handling
- [ ] Inventory updates on order
- [ ] Bulk stock updates
- [ ] Stock history/audit log

---

### 15. **Reviews & Ratings**

**Status**: ❌ NOT IMPLEMENTED

**Required**:
- [ ] Review model
- [ ] Star rating system
- [ ] Review submission form
- [ ] Review moderation (admin)
- [ ] Average rating calculation
- [ ] Review helpful votes

---

## 📝 Non-Functional Placeholder Features

### 16. **Visual Design Editor**

**Status**: 🔴 NON-FUNCTIONAL (see PROJECT_REVIEW.md)

**Issue**: Saves to database but doesn't apply to site

**Required**:
- [ ] ThemeContext provider
- [ ] CSS variable injection
- [ ] Dynamic Tailwind class generation
- [ ] Real-time theme application
- [ ] Theme preview that affects actual site

---

## 🎨 UI/UX Placeholders

### 17. **Generic Alert Messages**

**Status**: ⚠️ POOR UX

**Locations**:
- PostManager: `alert("Error saving post")`
- DesignEditor: `alert("Design saved successfully!")`

**Required**:
- [ ] Toast notification system
- [ ] Error boundaries with user-friendly messages
- [ ] Loading states with progress indicators
- [ ] Success confirmations

---

### 18. **No Loading States**

**Status**: ⚠️ INCONSISTENT

**Missing**:
- DesignEditor: No loading state when fetching design
- Some API calls show loading, others don't

**Required**:
- [ ] Consistent loading indicators across all async operations
- [ ] Skeleton screens for content loading
- [ ] Progress bars for uploads

---

## 📊 Priority Matrix

### Critical (Block Production)
1. 🔴 Authentication system
2. 🔴 Shopping cart functionality
3. 🔴 Checkout flow with payments
4. 🔴 Visual Design Editor functionality

### High Priority (Needed for MVP)
1. 🟡 Product detail page
2. 🟡 Order management
3. 🟡 Image upload
4. 🟡 Catalog page with filters
5. 🟡 Email system

### Medium Priority (Important Features)
1. 🟢 Category system
2. 🟢 Search functionality
3. 🟢 User dashboard
4. 🟢 Inventory management
5. 🟢 Toast notifications

### Low Priority (Nice to Have)
1. ⚪ Reviews & ratings
2. ⚪ Wishlist
3. ⚪ Newsletter
4. ⚪ Advanced filters
5. ⚪ Social sharing

---

## 🎯 Implementation Roadmap

### Phase 1: Essential Ecommerce (Week 1-2)
**Goal**: Make it a functional online store

1. ✅ Database models (already done)
2. **Shopping Cart**
   - Create CartContext
   - Add to cart functionality
   - Cart modal/page
   - Persistent cart (localStorage)
3. **Product Detail Page**
   - Create route and component
   - Image display
   - Add to cart button
4. **Basic Checkout**
   - Checkout form
   - Order creation
   - Order confirmation

**Deliverable**: Users can browse, add to cart, and place orders

---

### Phase 2: Payments & Auth (Week 3)
**Goal**: Secure payments and user accounts

1. **Stripe Integration**
   - Payment intent API
   - Stripe Elements component
   - Payment confirmation
2. **Authentication**
   - JWT implementation
   - Login/register pages
   - Protected routes
   - Admin-only access

**Deliverable**: Secure payment processing and user authentication

---

### Phase 3: Admin Tools (Week 4)
**Goal**: Complete admin panel

1. **Order Management**
   - Order list
   - Order details
   - Status updates
2. **Image Upload**
   - Upload endpoint
   - Frontend upload UI
   - Image storage
3. **Category Management**
   - Category CRUD
   - Product-category linking

**Deliverable**: Full admin control over store

---

### Phase 4: Enhanced UX (Week 5)
**Goal**: Better user experience

1. **Search & Filters**
   - Search functionality
   - Category filters
   - Price range filter
2. **User Dashboard**
   - Order history
   - Account settings
3. **Email Notifications**
   - Order confirmations
   - Password resets

**Deliverable**: Feature-complete ecommerce platform

---

### Phase 5: Polish & Optimization (Week 6)
**Goal**: Production-ready

1. **Fix Visual Design Editor** (make it functional)
2. **Toast Notifications**
3. **Error Boundaries**
4. **Performance Optimization**
5. **SEO Improvements**
6. **Security Audit**
7. **Testing**

**Deliverable**: Production-ready application

---

## 🔧 Quick Wins (Can Do Today)

### Easy Implementations (< 2 hours each)

1. **Product Detail Page** (basic version)
   - Create route
   - Display product info
   - Add to cart button

2. **Cart Context** (state only)
   - Create context
   - Add/remove items
   - Calculate total

3. **Toast Notifications**
   - Install `react-hot-toast`
   - Replace all `alert()` calls
   - Style toasts to match design

4. **Catalog Page** (basic)
   - Remove "próximamente"
   - Show all products
   - Basic filtering

5. **Image Upload UI** (frontend only)
   - File input component
   - Preview before upload
   - Upload button (can implement backend later)

---

## 📋 Placeholder Summary

**Total Placeholders Found**: 18

**By Type**:
- UI Placeholders: 4
- Non-functional Features: 3
- Missing Core Features: 11

**By Priority**:
- Critical: 4
- High: 5
- Medium: 5
- Low: 4

**Estimated Total Effort**: 8-10 weeks for complete implementation

**Next Immediate Steps**:
1. Implement shopping cart (2-3 days)
2. Create product detail page (1 day)
3. Add basic checkout (2-3 days)
4. Integrate Stripe payments (2 days)
5. Implement authentication (3-4 days)

---

**Document Last Updated**: 2025-10-16
