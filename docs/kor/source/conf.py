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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = '7616-multiLang'
copyright = '2024, Soyoon Choi'
author = 'Soyoon Choi'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'sphinx_search.extension',
]

myst_enable_extensions = [
    "deflist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ko'

#MyST meta insertion extension
myst_html_meta = {
    "description lang=en": "Altibase Manuals",
    "description lang=ko": "알티베이스 매뉴얼을 제공합니다",
    "keywords lang=en": "Altibase, Altibase manual, Altibase 7.1, Altibase 7.3, DBMS, Database",
    "keywords lang=ko": "알티베이스, 알티베이스 매뉴얼, 알티베이스 가이드, 알티베이스의 메타 프로토타입 키워드입니다",
    "property=og:locale":  "ko_KR",
    "property=og:locale:alternate ":"en_US"
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_favicon = 'faviconV2.ico'

html_build_dir = os.environ.get('READTHEDOCS_OUTPUT', 'docs/kor/build/html')

suppress_warnings = ["myst.header"]