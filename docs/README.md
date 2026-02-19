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

## Read the Docs

The documentation is configured to build automatically on Read the Docs using the `.readthedocs.yml` configuration file in the project root.
