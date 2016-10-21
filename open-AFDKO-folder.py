#MenuTitle: Open Temp/ folder (AFDKO build temporary files)
# -*- coding: utf-8 -*-
__doc__="""
Opens the Temp/ folder in ~/Library/Application support/Glyphs to access and diagnose build problems.
"""
__copyright__ = 'Copyright (c) 2016, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

import subprocess

path = os.path.expanduser('~/Library/Application Support/Glyphs/Temp')

print "Opening the Temp AFDKO folder: " + path

subprocess.call(["open", "-R", path])
