#MenuTitle: Open smith results/ folder
# -*- coding: utf-8 -*-
__doc__="""
Opens the results/ folder inside your project to get to the smith generated files.
"""

__copyright__ = 'Copyright (c) 2016, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

import subprocess

paths = Glyphs.defaults["org.sil.scripts.smith.ProjectPaths"]

print "Opening the results/ folder: "

subprocess.call(["open", "-R", paths + 'results'])
