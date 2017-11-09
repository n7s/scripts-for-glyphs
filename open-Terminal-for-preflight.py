#MenuTitle: Open Terminal to run preflight
# -*- coding: utf-8 -*-
__doc__="""
Opens the project folder root based on currently open source file to run preflight in your terminal
"""

__copyright__ = 'Copyright (c) 2017, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

import subprocess

projectpath = Glyphs.font.filepath
rootFolder = os.path.join(os.path.dirname(projectpath), '..')

subprocess.call(['open', '-a', 'Terminal', rootFolder])

Glyphs.showNotification('Run ./preflight in this folder', '(For %s %s.%s - %s)' % (Glyphs.font.familyName, Glyphs.font.versionMajor, Glyphs.font.versionMinor,  Glyphs.font.date))
