# Release script for CaPybara (PowerShell)

$VERSION = "0.1.0"
$TAG = "v$VERSION"

Write-Host "🚀 Preparing release $TAG..." -ForegroundColor Cyan

# Check if we're on main branch
$BRANCH = git rev-parse --abbrev-ref HEAD
if ($BRANCH -ne "main") {
    Write-Host "⚠️  Warning: You're not on the main branch (current: $BRANCH)" -ForegroundColor Yellow
    $response = Read-Host "Continue anyway? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        exit 1
    }
}

# Check for uncommitted changes
$status = git status --porcelain
if ($status) {
    Write-Host "❌ Error: You have uncommitted changes. Please commit or stash them first." -ForegroundColor Red
    exit 1
}

# Verify versions match
$PYTHON_VERSION = python -c "import sys; sys.path.insert(0, 'src'); import capybara; print(capybara.__version__)"
$PYPROJECT_VERSION = (Select-String -Path pyproject.toml -Pattern '^version = ' | ForEach-Object { $_.Line -replace 'version = "(.+)".*', '$1' })

if ($PYTHON_VERSION -ne $VERSION -or $PYPROJECT_VERSION -ne $VERSION) {
    Write-Host "❌ Error: Version mismatch!" -ForegroundColor Red
    Write-Host "  Python package: $PYTHON_VERSION"
    Write-Host "  pyproject.toml: $PYPROJECT_VERSION"
    Write-Host "  Expected: $VERSION"
    exit 1
}

Write-Host "✅ Versions verified: $VERSION" -ForegroundColor Green

# Build the package
Write-Host "📦 Building package..." -ForegroundColor Cyan
python -m build

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Build successful!" -ForegroundColor Green

# Check if tag already exists
$tagExists = git rev-parse "$TAG" 2>$null
if ($tagExists) {
    Write-Host "⚠️  Tag $TAG already exists!" -ForegroundColor Yellow
    $response = Read-Host "Delete and recreate? (y/N)"
    if ($response -eq "y" -or $response -eq "Y") {
        git tag -d "$TAG"
        git push origin ":refs/tags/$TAG" 2>$null
    } else {
        exit 1
    }
}

# Create tag
Write-Host "🏷️  Creating tag $TAG..." -ForegroundColor Cyan
$tagMessage = @"
Release $TAG

Initial release establishing the architectural foundation for warehouse introspection and visualization.

See CHANGELOG.md for details.
"@

git tag -a "$TAG" -m $tagMessage

Write-Host "✅ Tag created!" -ForegroundColor Green

Write-Host ""
Write-Host "📋 Next steps:" -ForegroundColor Cyan
Write-Host "  1. Review the built package in dist/"
Write-Host "  2. Push commits: git push origin main"
Write-Host "  3. Push tag: git push origin $TAG"
Write-Host "  4. (Optional) Test on Test PyPI: twine upload --repository testpypi dist/*"
Write-Host "  5. (Optional) Publish to PyPI: twine upload dist/*"
Write-Host "  6. Create GitHub Release with notes from CHANGELOG.md"
Write-Host ""
Write-Host "✨ Release $TAG is ready!" -ForegroundColor Green
