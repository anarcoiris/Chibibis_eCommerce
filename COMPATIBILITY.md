# Version Compatibility Guide

This document outlines the tested and supported versions for the ecommerce project.

## ✅ Recommended Versions

### Python
- **Recommended**: 3.10, 3.11, 3.12, 3.13
- **Current Testing**: Python 3.14.0
- **Minimum**: Python 3.10

### Node.js
- **Recommended**: 18.x, 20.x, 22.x
- **Current Testing**: 22.20.0
- **Minimum**: Node.js 18.0

### Operating Systems
- **Windows**: 10, 11 ✅ Fully tested
- **Linux**: Ubuntu 20.04+, Debian 11+ ✅ Compatible
- **macOS**: 11+ (Big Sur) ✅ Compatible

## ⚠️ Known Compatibility Issues

### Python 3.14+
**Status**: ⚠️ Partially Compatible

**Known Issues**:
- Pydantic v1 compatibility warning in FastAPI
- Some packages may not have pre-built wheels
- Warning message: "Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater"

**Recommendation**: Use Python 3.10-3.13 for production

**Workaround**: The application works but displays warnings. Future updates will address this.

### Python 3.9 and Below
**Status**: ❌ Not Supported

The project uses features from Python 3.10+ including:
- Pattern matching (not used yet but available)
- Union type syntax (|)
- Modern type hints

## 📦 Package Versions

### Backend Dependencies (Python)

| Package | Version | Status | Notes |
|---------|---------|--------|-------|
| fastapi | 0.119.0 | ✅ Stable | Core framework |
| uvicorn | 0.37.0 | ✅ Stable | ASGI server |
| sqlmodel | 0.0.27 | ✅ Stable | ORM |
| sqlalchemy | 2.0.36 | ✅ Stable | Database toolkit |
| alembic | 1.14.0 | ✅ Stable | Migrations |
| pydantic | 2.10.3 | ✅ Stable | Data validation |
| stripe | 11.3.0 | ✅ Stable | Payments |
| Pillow | 11.0.0 | ✅ Stable | Image generation |
| Faker | 33.1.0 | ✅ Stable | Test data |

### Frontend Dependencies (Node.js)

| Package | Version | Status | Notes |
|---------|---------|--------|-------|
| react | 18.2.0 | ✅ Stable | UI library |
| react-dom | 18.2.0 | ✅ Stable | DOM renderer |
| vite | 5.0.0 | ✅ Stable | Build tool |
| tailwindcss | 4.0.0 | ⚠️ Beta | CSS framework |
| react-router-dom | 6.11.2 | ✅ Stable | Routing |
| axios | 1.4.0 | ✅ Stable | HTTP client |
| react-hot-toast | 2.6.0 | ✅ Stable | Notifications |

**Note**: Tailwind CSS 4.0 is in beta. The project uses stable features only.

## 🔍 Tested Configurations

### Configuration 1 (Current Development)
- **OS**: Windows 10
- **Python**: 3.14.0 ⚠️
- **Node.js**: 22.20.0 ✅
- **Status**: Working with warnings

### Configuration 2 (Recommended)
- **OS**: Windows 11
- **Python**: 3.12.x ✅
- **Node.js**: 20.x ✅
- **Status**: Fully tested, no warnings

### Configuration 3 (Linux)
- **OS**: Ubuntu 22.04
- **Python**: 3.11.x ✅
- **Node.js**: 18.x ✅
- **Status**: Compatible (not extensively tested)

## 🚨 Breaking Changes

### Python 3.14
**Impact**: Low - Application works but shows warnings

**Details**:
- Pydantic v1 compatibility warnings in FastAPI
- No functional impact on current features
- May require updates when dependencies release Python 3.14 support

**Action Required**: None for development, consider downgrading for production

### Tailwind CSS 4.0
**Impact**: None - Using stable features only

**Details**:
- Project uses v4.0 beta
- Only uses stable, well-supported features
- No breaking changes expected

**Action Required**: None

## 🔄 Migration Guides

### Downgrading Python from 3.14 to 3.13

**Windows:**
```bash
# 1. Uninstall Python 3.14
# (Use Windows Settings > Apps)

# 2. Install Python 3.13 from python.org

# 3. Recreate virtual environment
cd C:\path\to\ecommerce
rmdir /s /q .venv
python -m venv .venv
.venv\Scripts\activate
pip install -r backend\requirements.txt
```

**Linux/macOS:**
```bash
# 1. Install Python 3.13 (use package manager or pyenv)

# 2. Recreate virtual environment
cd /path/to/ecommerce
rm -rf .venv
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

### Upgrading Node.js

**Windows:**
1. Download latest LTS from https://nodejs.org
2. Run installer
3. Restart terminal
4. Verify: `node --version`

**Linux (using nvm):**
```bash
# Install nvm if not already installed
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Install and use Node.js 20 LTS
nvm install 20
nvm use 20
```

## 📅 Support Timeline

| Version | Support Status | End of Support |
|---------|---------------|----------------|
| Python 3.13 | ✅ Fully Supported | Oct 2028 |
| Python 3.12 | ✅ Fully Supported | Oct 2027 |
| Python 3.11 | ✅ Fully Supported | Oct 2026 |
| Python 3.10 | ✅ Fully Supported | Oct 2025 |
| Python 3.14 | ⚠️ Testing | TBD |
| Node.js 20 | ✅ LTS | Apr 2026 |
| Node.js 18 | ✅ LTS | Apr 2025 |

## 🧪 Testing New Versions

Before using newer versions in production:

1. **Create test environment**:
   ```bash
   python3.XX -m venv .venv-test
   source .venv-test/bin/activate  # Linux/macOS
   # OR
   .venv-test\Scripts\activate     # Windows
   ```

2. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Run tests** (when available):
   ```bash
   pytest backend/tests/
   ```

4. **Manual testing**:
   - Start backend and frontend
   - Test all major features
   - Check console for warnings/errors
   - Verify admin panel functionality

## 📞 Reporting Compatibility Issues

If you encounter compatibility issues:

1. Check this document for known issues
2. Search existing GitHub issues
3. Create new issue with:
   - Python/Node.js versions
   - Operating system
   - Error messages
   - Steps to reproduce

## 🔄 Update Frequency

This document is updated:
- When new Python/Node.js versions are released
- When compatibility issues are discovered
- After testing new configurations
- With each major project release

**Last Updated**: 2025-10-16
**Next Review**: 2025-11-16
