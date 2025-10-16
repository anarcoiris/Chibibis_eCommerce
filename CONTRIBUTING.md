# Contributing to Ecommerce Project

Thank you for considering contributing to the ecommerce starter project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

**Before submitting a bug report**:
- Check the [COMPATIBILITY.md](COMPATIBILITY.md) for known version issues
- Search existing [GitHub issues](https://github.com/anarcoiris/Chibibis_eCommerce/issues)
- Check [PROJECT_REVIEW.md](PROJECT_REVIEW.md) for known limitations

**When submitting a bug report, include**:
- Python and Node.js versions (`python --version`, `node --version`)
- Operating system and version
- Steps to reproduce the issue
- Expected vs actual behavior
- Error messages (console logs, terminal output)
- Screenshots if applicable

### Suggesting Features

**Before suggesting a feature**:
- Check [PLACEHOLDERS_AND_MISSING_FEATURES.md](PLACEHOLDERS_AND_MISSING_FEATURES.md) for planned features
- Search existing GitHub issues for similar suggestions

**When suggesting a feature, include**:
- Clear description of the feature
- Use case and benefits
- Proposed implementation (if you have ideas)
- Mockups or examples (if applicable)

## 💻 Development Setup

### Prerequisites
- Python 3.10-3.13
- Node.js 18+
- Git

### Setup Instructions

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Chibibis_eCommerce.git
   cd Chibibis_eCommerce
   ```

2. **Run automated setup**:
   ```bash
   # Windows
   setup.bat

   # Linux/macOS
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Code Standards

### Python (Backend)

**Style Guide**: Follow PEP 8

```python
# Good
def calculate_total(items: list[dict]) -> float:
    """Calculate total price of items."""
    return sum(item['price'] * item['quantity'] for item in items)

# Bad
def calc(x):
    return sum([i['price']*i['quantity'] for i in x])
```

**Naming Conventions**:
- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_CASE`
- Private methods: `_leading_underscore`

**Type Hints**: Always use type hints for function parameters and return values

**Docstrings**: Use docstrings for all functions, classes, and modules

### JavaScript/React (Frontend)

**Style Guide**: Follow Airbnb JavaScript Style Guide

```javascript
// Good
export default function ProductCard({ product }) {
  const { addItem } = useCart();

  const handleAddToCart = () => {
    addItem(product);
  };

  return (
    <article className="product-card">
      {/* content */}
    </article>
  );
}

// Bad
function ProductCard(props) {
  return <div onClick={()=>props.addItem(props.product)}>stuff</div>
}
```

**Naming Conventions**:
- Components: `PascalCase`
- Functions and variables: `camelCase`
- Constants: `UPPER_CASE`
- Files: Match component name (`ProductCard.jsx`)

**Component Structure**:
1. Imports
2. Component definition
3. Hooks
4. Event handlers
5. Return JSX

**Styling**:
- Use Tailwind CSS utilities
- Avoid inline styles unless dynamic (theme colors)
- Use `className` for static styles
- Use `style` for dynamic theme-based styles

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

**Note**: Testing infrastructure is not fully implemented yet. Contributions welcome!

## 🔀 Pull Request Process

### Before Submitting

1. **Test your changes**:
   ```bash
   # Backend
   cd backend
   python -m uvicorn backend.app.main:app --reload

   # Frontend
   cd frontend
   npm run dev
   ```

2. **Check for errors**:
   - No console errors in browser
   - No Python exceptions in terminal
   - Features work as expected

3. **Update documentation**:
   - Update README.md if adding features
   - Add to CHANGELOG.md (under [Unreleased])
   - Update relevant documentation files

### Submitting Pull Request

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add feature: brief description

   - Detailed point 1
   - Detailed point 2

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude <noreply@anthropic.com>"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**:
   - Go to GitHub repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the template

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Changes Made
- Change 1
- Change 2

## Testing
- [ ] Tested locally
- [ ] No console errors
- [ ] Features work as expected

## Screenshots (if applicable)
Add screenshots here

## Related Issues
Closes #123
```

## 📁 Project Structure

Understanding the project structure helps contribute effectively:

```
ecommerce/
├─ backend/backend/app/
│  ├─ main.py              # FastAPI app entry
│  ├─ models/              # Database models
│  ├─ schemas/             # Pydantic schemas
│  ├─ api/v1/              # API endpoints
│  ├─ db/                  # Database config
│  └─ core/                # Settings
├─ frontend/src/
│  ├─ components/          # Reusable components
│  ├─ context/             # React contexts
│  ├─ pages/               # Page components
│  └─ App.jsx              # Root component
└─ scripts/                # Utility scripts
```

## 🎯 Areas Needing Contribution

### High Priority
- [ ] Authentication system (JWT)
- [ ] Unit and integration tests
- [ ] Product detail pages
- [ ] Checkout flow
- [ ] Image upload functionality

### Medium Priority
- [ ] Search functionality
- [ ] Category system
- [ ] User dashboard
- [ ] Order management

### Documentation
- [ ] API documentation improvements
- [ ] Component documentation
- [ ] Tutorial videos or guides
- [ ] Translation to other languages

## 🚫 What Not to Do

- Don't commit to `main` branch directly
- Don't include sensitive information (API keys, passwords)
- Don't commit large binary files
- Don't mix multiple unrelated changes in one PR
- Don't commit `node_modules/`, `.venv/`, or `ecommerce.db`
- Don't remove existing features without discussion

## 💡 Tips for Good Contributions

1. **Start small**: Fix typos, improve documentation, add comments
2. **Communicate**: Open an issue before working on large features
3. **Follow conventions**: Match existing code style
4. **Test thoroughly**: Test on multiple browsers/OS if possible
5. **Document changes**: Update relevant documentation
6. **Be patient**: Reviews may take time

## 📞 Getting Help

- **Questions**: Open a GitHub issue with [Question] tag
- **Discussion**: Use GitHub Discussions
- **Documentation**: Check [DOCUMENTATION.md](DOCUMENTATION.md)

## 🏆 Recognition

Contributors will be:
- Listed in README.md contributors section (when created)
- Credited in CHANGELOG.md for their contributions
- Appreciated with GitHub stars and thanks! ⭐

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to make this project better! 🎉
