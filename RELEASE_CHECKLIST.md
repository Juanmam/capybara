# Release Checklist

Use this checklist when preparing a new release.

## Pre-Release

- [ ] Update version in `src/capybara/__init__.py`
- [ ] Update version in `pyproject.toml`
- [ ] Update `CHANGELOG.md` with release notes
- [ ] Review and update `README.md` if needed
- [ ] Ensure all tests pass (when available)
- [ ] Verify documentation is up to date
- [ ] Check that all dependencies are correctly specified

## Build and Test

- [ ] Build the package locally: `python -m build`
- [ ] Verify the built package structure
- [ ] Test installation: `pip install dist/capybara-*.whl`
- [ ] Verify package metadata is correct

## Git Operations

- [ ] Commit all changes
- [ ] Create annotated git tag: `git tag -a v0.1.0 -m "Release v0.1.0"`
- [ ] Push commits: `git push origin main`
- [ ] Push tags: `git push origin v0.1.0`

## Publishing (Optional)

- [ ] Test on Test PyPI: `twine upload --repository testpypi dist/*`
- [ ] Verify Test PyPI installation works
- [ ] Publish to PyPI: `twine upload dist/*`

## Post-Release

- [ ] Create GitHub Release with release notes
- [ ] Update version to next development version (e.g., 0.1.1-dev)
- [ ] Announce release (if applicable)

## Current Release: v0.1.0

### Version Information
- Version: `0.1.0`
- Release Date: 2026-02-19
- Status: Initial release - Architectural foundation

### What's Included
- Complete architectural foundation
- Domain models and abstractions
- Documentation structure
- Packaging configuration
- GitHub Pages integration

### What's Not Included (Future)
- FabricWarehouse implementation
- Inference rule implementations
- Diagram rendering implementations
- Integration between layers
