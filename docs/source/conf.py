# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'repo-sanitize'
copyright = '2025, William R. Astley / Pr1m8'
author = 'William R. Astley / Pr1m8'
release = '0.1.0'
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Adjust path to project root
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "myst_parser",
    "sphinx_copybutton",
]
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
autosummary_generate = True
todo_include_todos = True


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
