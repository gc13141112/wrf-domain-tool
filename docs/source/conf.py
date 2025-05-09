# conf.py — Sphinx configuration file

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add project root or relevant source directory to sys.path
sys.path.insert(0, os.path.abspath('../../wrf-domain-tool'))

# -- Project information -----------------------------------------------------

project = 'wrf-domain-tool'
author = '叩一人'
release = '0.1.0'  # Update with your version
copyright = '2023–2025, 叩一人'

# -- General configuration ---------------------------------------------------

# extensions = [
#     'sphinx.ext.autodoc',            # Automatic documentation from docstrings
#     'sphinx.ext.napoleon',           # Google and NumPy style docstring support
#     'sphinx.ext.viewcode',           # Add links to highlighted source code
#     'sphinx_autodoc_typehints',      # Use type hints in function signatures
# ]

# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'show-inheritance': True,
}

# Napoleon settings (optional tweaks)
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_use_param = True
# napoleon_use_rtype = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False  # 去除“Built with Sphinx”
html_show_copyright = False  # 不显示默认版权（我们自定义）
templates_path = ['_templates']
html_static_path = ['_static']
# html_theme_options = {
#     'navigation_depth': 4,
#     'collapse_navigation': False,
# }

# -- Options for typehints ---------------------------------------------------

# typehints_fully_qualified = False  # Display just class names, not full paths
