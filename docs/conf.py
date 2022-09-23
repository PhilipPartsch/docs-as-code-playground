# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information

project = 'Docs-As-Code Playground'
copyright = '2022, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.0'

# -- General configuration

on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    #'sphinx.ext.intersphinx',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# sphinxcontrib.plantuml configuration

# local_plantuml_path is from https://github.com/useblocks/sphinx-needs/blob/master/docs/conf.py
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")
print (local_plantuml_path)

if on_rtd:
    # Deactivated using rtd plantuml version as it looks quite old.
    # plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

plantuml_output_format = 'svg'

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
