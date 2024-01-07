# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ebl_utils'
copyright = '2024, Jordan Mirocha'
author = 'Jordan Mirocha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax',
    'sphinx.ext.viewcode', 'numpydoc', 'nbsphinx', 'm2r2']

templates_path = ['_templates']
exclude_patterns = []

# The suffix of source filenames.
source_suffix = [".rst", ".md"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'default'
html_static_path = ['_static']

# The master toctree document.
master_doc = 'index'
