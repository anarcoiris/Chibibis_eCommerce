# Ecommerce Project - Documentation Index

Complete documentation index for the ecommerce starter project.

## 📖 Getting Started

### For New Users
1. **[README.md](README.md)** - Project overview and quick start
2. **[SETUP.md](SETUP.md)** - Detailed installation and setup guide
3. **[COMPATIBILITY.md](COMPATIBILITY.md)** - Version compatibility information

### For Developers
1. **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project
2. **[CHANGELOG.md](CHANGELOG.md)** - Version history and changes
3. **[CLAUDE.md](CLAUDE.md)** - Instructions for Claude Code AI assistant

## 🎨 User Guides

### Frontend Features
- **[DESIGN_GUIDE.md](DESIGN_GUIDE.md)** - UI/UX design system and component guide
  - Animated background specifications
  - Color palette and typography
  - Component patterns
  - Responsive design breakpoints
  - Animation guidelines

### Admin Panel
- **[ADMIN_PANEL.md](ADMIN_PANEL.md)** - Complete admin panel documentation
  - Content management (posts, pages, banners)
  - Visual design editor usage
  - API endpoints reference
  - Database models
  - Best practices

## 🛠️ Technical Documentation

### Architecture
- **[PROJECT_REVIEW.md](PROJECT_REVIEW.md)** - Critical analysis and technical debt assessment
  - Known issues and limitations
  - Security audit
  - Performance metrics
  - Code quality assessment

### Features & Roadmap
- **[PLACEHOLDERS_AND_MISSING_FEATURES.md](PLACEHOLDERS_AND_MISSING_FEATURES.md)** - Feature inventory and roadmap
  - Identified placeholders
  - Missing core features
  - Priority matrix
  - Implementation roadmap (6-week plan)
  - Quick wins

## 🚀 Quick Reference

### Installation Commands

**Windows (First Time):**
```bash
# Automated setup
setup.bat

# Interactive launcher
launcher.bat
```

**Linux/macOS (First Time):**
```bash
# Make executable and run
chmod +x setup.sh
./setup.sh
```

### Running the Application

**Windows:**
```bash
start-all.bat           # Start all servers
launcher.bat            # Interactive menu
start-backend.bat       # Backend only
start-frontend.bat      # Frontend only
```

**Linux/macOS:**
```bash
./start-backend.sh      # Backend
./start-frontend.sh     # Frontend
```

### Access URLs

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:5173 | Main application |
| Admin Panel | http://localhost:5173/admin | Content management |
| Backend API | http://localhost:8000 | REST API |
| API Docs (Swagger) | http://localhost:8000/docs | Interactive API documentation |
| ReDoc | http://localhost:8000/redoc | Alternative API documentation |

## 📁 Project Structure

```
ecommerce/
├─ backend/                      # FastAPI backend
│  ├─ backend/app/              # Application code
│  │  ├─ main.py               # Entry point
│  │  ├─ models/               # Database models
│  │  ├─ schemas/              # Pydantic schemas
│  │  ├─ api/v1/               # API endpoints
│  │  ├─ db/                   # Database config
│  │  └─ core/                 # Settings
│  ├─ alembic/                 # Database migrations
│  ├─ requirements.txt         # Python dependencies
│  └─ ecommerce.db            # SQLite database
├─ frontend/                    # React frontend
│  ├─ src/
│  │  ├─ components/           # UI components
│  │  ├─ context/              # React contexts (Theme, Cart)
│  │  ├─ pages/                # Page components
│  │  └─ main.jsx              # Entry point
│  ├─ package.json            # Node dependencies
│  └─ vite.config.js          # Vite configuration
├─ scripts/                     # Utility scripts
│  └─ gen_placeholders.py      # Generate sample data
├─ docs/                        # Additional documentation
│  └─ development/             # Development notes
├─ setup.bat / setup.sh         # Automated setup scripts
├─ launcher.bat                 # Interactive menu (Windows)
├─ start-all.bat               # Start all servers (Windows)
├─ start-backend.bat/sh        # Start backend
├─ start-frontend.bat/sh       # Start frontend
└─ README.md                   # Project overview
```

## 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `backend/requirements.txt` | Python package dependencies with fixed versions |
| `frontend/package.json` | Node.js dependencies |
| `backend/.env.example` | Environment variables template |
| `frontend/vite.config.js` | Vite dev server configuration |
| `backend/alembic.ini` | Database migration configuration |
| `.gitignore` | Git ignore rules |

## 🎯 Feature Documentation

### Implemented Features

1. **Dynamic Theme System** (See [DESIGN_GUIDE.md](DESIGN_GUIDE.md))
   - Live color customization
   - Font selection (heading & body)
   - Layout options (border radius, spacing)
   - Real-time preview

2. **Shopping Cart** (See [PLACEHOLDERS_AND_MISSING_FEATURES.md](PLACEHOLDERS_AND_MISSING_FEATURES.md))
   - Add/remove items
   - Quantity management
   - localStorage persistence
   - Cart modal with checkout button

3. **Admin Panel** (See [ADMIN_PANEL.md](ADMIN_PANEL.md))
   - Content management (posts, pages, banners)
   - Visual design editor
   - Database-backed storage

4. **Animated Background** (See [DESIGN_GUIDE.md](DESIGN_GUIDE.md))
   - Particle network (80 particles)
   - Mouse interaction
   - Breathing gradient effect
   - Performance optimized (60fps)

### Planned Features

See [PLACEHOLDERS_AND_MISSING_FEATURES.md](PLACEHOLDERS_AND_MISSING_FEATURES.md) for complete roadmap.

## 🐛 Troubleshooting

### Common Issues

**Setup fails:**
- Check Python version (3.10-3.13 recommended)
- Check Node.js version (18+ required)
- See [COMPATIBILITY.md](COMPATIBILITY.md)

**Backend won't start:**
- Ensure virtual environment is activated
- Check port 8000 is not in use
- Review [SETUP.md](SETUP.md) troubleshooting section

**Frontend won't start:**
- Ensure node_modules are installed
- Check port 5173 is not in use
- Try deleting node_modules and reinstalling

**Theme changes not applying:**
- Check backend is running
- Clear browser cache
- See [PROJECT_REVIEW.md](PROJECT_REVIEW.md) for known issues

## 📞 Support & Contributing

- **Issues**: Report bugs or request features via GitHub issues
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- **Documentation**: All documentation files are in markdown format

## 📊 Version Information

- **Current Version**: 0.3.0
- **Last Updated**: 2025-10-16
- **Python**: 3.10-3.13 (3.14+ not fully tested)
- **Node.js**: 18+

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.
