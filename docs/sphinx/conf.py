"""Sphinx configuration for CaPybara documentation."""

import os
import sys
from datetime import datetime

# Add the src directory to the path so autodoc can find the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# Project information
project = 'CaPybara'
copyright = f'{datetime.now().year}, Juan Manuel Mejía Botero'
author = 'Juan Manuel Mejía Botero'

# Get version from package
import capybara
release = capybara.__version__
version = '.'.join(release.split('.')[:2])  # Major.minor version

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
]

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__',
}

autosummary_generate = True
autosummary_imported_members = True

# Napoleon settings for Google/NumPy style docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Type hints settings
typehints_fully_qualified = False
always_document_param_types = True
typehints_document_rtype = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Templates
templates_path = ['_templates']

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output options
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# Theme options
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# HTML output
html_title = f'CaPybara {version} Documentation'
html_short_title = 'CaPybara'
html_logo = None
html_favicon = None

# Output file base name for HTML help builder
htmlhelp_basename = 'capybaradoc'

# LaTeX options
latex_elements = {}
latex_documents = [
    ('index', 'capybara.tex', 'CaPybara Documentation',
     'Juan Manuel Mejía Botero', 'manual'),
]

# Man page options
man_pages = [
    ('index', 'capybara', 'CaPybara Documentation',
     [author], 1)
]

# Texinfo options
texinfo_documents = [
    ('index', 'capybara', 'CaPybara Documentation',
     author, 'CaPybara', 'Data-driven Python library for warehouse introspection and visualization',
     'Miscellaneous'),
]

# EPUB options
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
