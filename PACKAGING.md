# Packaging and Distribution Guide

This document describes how to package and distribute CaPybara.

## Building the Package

### Prerequisites

Install build tools:

```bash
pip install build twine
```

### Building Source and Wheel Distributions

```bash
python -m build
```

This will create:
- `dist/capybara-0.1.0.tar.gz` - Source distribution
- `dist/capybara-0.1.0-py3-none-any.whl` - Wheel distribution

## Publishing to PyPI

### Test PyPI (for testing)

```bash
# Upload to test PyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ capybara
```

### Production PyPI

```bash
# Upload to production PyPI
twine upload dist/*
```

**Note**: You'll need PyPI credentials. Create an account at https://pypi.org and configure credentials using `twine` or `.pypirc`.

## Version Management

Update the version in:
- `src/capybara/__init__.py` - `__version__` variable
- `pyproject.toml` - `version` field

Follow semantic versioning (MAJOR.MINOR.PATCH).

## Read the Docs Setup

1. Create an account at https://readthedocs.org
2. Import your repository
3. Configure the project:
   - Python version: 3.11
   - Configuration file: `.readthedocs.yml`
   - Install requirements from: `docs/requirements.txt`
4. Build the documentation

The documentation will be automatically built on each commit to the main branch.

## Local Documentation Build

See `docs/README.md` for instructions on building documentation locally.
