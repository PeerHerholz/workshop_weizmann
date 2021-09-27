# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'gorella_base'
copyright = '2020, G0RELLA'
author = 'Peer Herholz, José C. García Alanis, Christoph Vogelbacher'

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = ""
html_theme = "sphinx_book_theme"
html_logo = "_static/gorella_logo.png"
html_theme_options = {
    "github_url": "https://github.com/G0RELLA/gorella_base",
    "repository_url": "https://github.com/G0RELLA/gorella_base",
    "repository_branch": "master",
    "use_edit_page_button": True,
    "path_to_docs": "docs/",
    "expand_sections": ["use/index", "examples/index"],
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "jb": ("https://jupyterbook.org/", None),
    "myst": ("https://myst-parser.readthedocs.io/en/latest/", None),
    "markdown_it": ("https://markdown-it-py.readthedocs.io/en/latest", None),
    "nbclient": ("https://nbclient.readthedocs.io/en/latest", None),
    "nbformat": ("https://nbformat.readthedocs.io/en/latest", None),
    "sphinx": ("https://www.sphinx-doc.org/en/3.x", None),
}

intersphinx_cache_limit = 5

nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.nodes.Node"),
    ("py:class", "docutils.nodes.container"),
    ("py:class", "docutils.nodes.system_message"),
    ("py:class", "nbformat.notebooknode.NotebookNode"),
    ("py:class", "pygments.lexer.RegexLexer"),
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]

copybutton_selector = "div:not(.output) > div.highlight pre"

nb_custom_formats = {".Rmd": ["jupytext.reads", {"fmt": "Rmd"}]}
jupyter_execute_notebooks = "cache"
execution_show_tb = "READTHEDOCS" in os.environ
execution_timeout = 60  # Note: 30 was timing out on RTD

myst_admonition_enable = True
myst_amsmath_enable = True
myst_html_img_enable = True
myst_deflist_enable = True
myst_url_schemes = ("http", "https", "mailto")
panels_add_boostrap_css = False
