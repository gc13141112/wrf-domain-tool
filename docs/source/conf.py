# conf.py — Sphinx configuration file

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add project root or relevant source directory to sys.path
sys.path.insert(0, os.path.abspath('../../wrf-domain-tool'))

# -- Project information -----------------------------------------------------

project = 'wrf-domain-tool'
author = 'Your Name or Organization'
release = '0.1.0'  # Update with your version

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',            # Automatic documentation from docstrings
    'sphinx.ext.napoleon',           # Google and NumPy style docstring support
    'sphinx.ext.viewcode',           # Add links to highlighted source code
    'sphinx_autodoc_typehints',      # Use type hints in function signatures
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}

# Napoleon settings (optional tweaks)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}

# -- Options for typehints ---------------------------------------------------

typehints_fully_qualified = False  # Display just class names, not full paths
