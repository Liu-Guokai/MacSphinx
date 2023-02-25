# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MacSphinx'
copyright = '2023, LiuGuokai'
author = 'LiuGuokai'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output



# import sphinx_theme
# html_theme = 'stanford_theme'
# html_theme_path = [sphinx_theme.get_html_theme_path('stanford-theme')]
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# support markdown
extensions = [
     'recommonmark',
    #  'sphinx_markdown_tables'
 ]



html_sidebars = {
    '**': [
        'versioning.html',
    ],
}
smv_latest_version = 'v3.0' 
sitemap_url_scheme = "{link}"