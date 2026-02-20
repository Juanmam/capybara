#!/bin/bash
# Release script for CaPybara

set -e

VERSION="0.1.0"
TAG="v${VERSION}"

echo "🚀 Preparing release ${TAG}..."

# Check if we're on main branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
    echo "⚠️  Warning: You're not on the main branch (current: $BRANCH)"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo "❌ Error: You have uncommitted changes. Please commit or stash them first."
    exit 1
fi

# Verify versions match
PYTHON_VERSION=$(python -c "import sys; sys.path.insert(0, 'src'); import capybara; print(capybara.__version__)")
PYPROJECT_VERSION=$(grep -E '^version = ' pyproject.toml | sed "s/version = \"\(.*\)\"/\1/")

if [ "$PYTHON_VERSION" != "$VERSION" ] || [ "$PYPROJECT_VERSION" != "$VERSION" ]; then
    echo "❌ Error: Version mismatch!"
    echo "  Python package: $PYTHON_VERSION"
    echo "  pyproject.toml: $PYPROJECT_VERSION"
    echo "  Expected: $VERSION"
    exit 1
fi

echo "✅ Versions verified: $VERSION"

# Build the package
echo "📦 Building package..."
python -m build

if [ $? -ne 0 ]; then
    echo "❌ Build failed!"
    exit 1
fi

echo "✅ Build successful!"

# Check if tag already exists
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "⚠️  Tag $TAG already exists!"
    read -p "Delete and recreate? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git tag -d "$TAG"
        git push origin ":refs/tags/$TAG" 2>/dev/null || true
    else
        exit 1
    fi
fi

# Create tag
echo "🏷️  Creating tag $TAG..."
git tag -a "$TAG" -m "Release $TAG

Initial release establishing the architectural foundation for warehouse introspection and visualization.

See CHANGELOG.md for details."

echo "✅ Tag created!"

echo ""
echo "📋 Next steps:"
echo "  1. Review the built package in dist/"
echo "  2. Push commits: git push origin main"
echo "  3. Push tag: git push origin $TAG"
echo "  4. (Optional) Test on Test PyPI: twine upload --repository testpypi dist/*"
echo "  5. (Optional) Publish to PyPI: twine upload dist/*"
echo "  6. Create GitHub Release with notes from CHANGELOG.md"
echo ""
echo "✨ Release $TAG is ready!"
