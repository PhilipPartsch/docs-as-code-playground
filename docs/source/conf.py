# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    #'sphinx.ext.intersphinx',
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# sphinxcontrib.plantuml configuration
tool_folder = os.path.join(os.getcwd(), "utils")
plantuml_path = os.path.join(tool_folder, "plantuml.jar")
plantuml = 'java -Djava.awt.headless=true -jar %s' % plantuml_path

# sphinx_needs configuration
needs_id_regex = '^[A-Za-z0-9_]{3,}'

# Define project specific needs directives
needs_types = [
               dict(directive="cust_req", title="Customer Requirement", prefix="CSTRQ_", color="#abcdef", style="artifact"),
               dict(directive="sys_req", title="System Requirement", prefix="SYSRQ_", color="#abcdef", style="artifact"),
               dict(directive="sw_req", title="Software Requirement", prefix="SWRQ_", color="#abcdef", style="artifact"),
               dict(directive="sys_test", title="System Test", prefix="SYSTST_", color="#abcdef", style="artifact"),
               dict(directive="sw_test", title="Software Test", prefix="SWTST_", color="#abcdef", style="artifact"),
              ]

# Define extra options for needs object
needs_extra_options = [
 'safety_level',
 'test_type',
]

# sphinx.ext.intersphinx configuration

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']
