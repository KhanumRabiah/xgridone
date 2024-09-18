# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xgridone'
copyright = '2024, RabiahK'
author = 'RabiahK'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'root'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
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