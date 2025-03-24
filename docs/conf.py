# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xgridone'
copyright = '2025, Rabiah Khanum'
author = 'Rabiah Khanum'
release = 'infinity'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    "bodyfont": "Times New Roman",
    "headfont": "Times New Roman",
    "linkcolor":"#4169E1",
    "visitedlinkcolor": "#B2BEB5",
    "bgcolor": "#F0FFFF",
    "headbgcolor": "#CCCCFF",
    "sidebarbgcolor": "#A7C7E7",
    "headtextcolor": "#301934",
    "sidebartextcolor": "191970",
    "sidebarlinkcolor": "#191970"
}

html_static_path = ['_static']

html_context = {
    'prev_page': 'Previous topic',  # Customize Previous button text
    'next_page': 'Next topic',      # Customize Next button text
}