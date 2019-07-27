#MenuTitle: where is my file?
# -*- coding: utf-8 -*-
__doc__="""
show the path of the currently active glyphs file (and versions)
"""

__copyright__ = 'Copyright (c) 2019, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'


import subprocess

Glyphs.showNotification('My current glyphs file:', '%s, version %s.%s (%s %s)' % (Glyphs.font.filepath, Glyphs.font.versionMajor, Glyphs.font.versionMinor, Glyphs.versionString, Glyphs.buildNumber))

path = Glyphs.font.filepath

subprocess.call(["open", "-R", path])
