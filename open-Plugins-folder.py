#MenuTitle: Open Plugins/ folder
# -*- coding: utf-8 -*-
__doc__="""
Opens the Plugins/ folder in ~/Library/Application support/Glyphs to access and diagnose problems.
"""

__copyright__ = 'Copyright (c) 2016, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

import subprocess

path = os.path.expanduser('~/Library/Application Support/Glyphs/Plugins')

print path

subprocess.call(["open", "-R", path])
