import os
import sys

project = 'Crypton'
copyright = '2022, Batuhan Inan'
author = 'Batuhan Inan'

release = '1.3'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

exclude_patterns = []

html_theme = 'furo'

html_static_path = ['_static']

sys.path.insert(0, os.path.abspath('../..'))  # Source code dir relative to this file

extensions = [
	'sphinx.ext.autodoc',  # Core library for html generation from docstrings
	'sphinx.ext.autosummary',  # Create neat summary tables
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
