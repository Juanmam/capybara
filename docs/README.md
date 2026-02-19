# CaPybara Documentation

This directory contains the documentation for CaPybara.

## Building the Documentation

### Prerequisites

Install the documentation dependencies:

```bash
pip install -e ".[docs]"
```

### Building Locally

Navigate to the `docs/sphinx` directory and run:

```bash
# On Linux/Mac
make html

# On Windows
make.bat html
```

The built documentation will be in `docs/sphinx/_build/html/`.

### Building with Sphinx directly

```bash
cd docs/sphinx
sphinx-build -b html . _build/html
```

## Documentation Structure

- `sphinx/` - Sphinx source files
  - `conf.py` - Sphinx configuration
  - `index.rst` - Main documentation index
  - `api/` - API documentation
  - `_static/` - Static files (CSS, images)
  - `_templates/` - Custom templates

## GitHub Pages

The documentation is automatically built and deployed to GitHub Pages using GitHub Actions. The workflow is configured in `.github/workflows/docs.yml`.

To enable GitHub Pages:
1. Go to your repository Settings → Pages
2. Set Source to "GitHub Actions"
3. The documentation will be automatically deployed on each push to the main branch
