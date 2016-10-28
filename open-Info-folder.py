#MenuTitle: Open Info/ folder (GlyphsData.xml)
# -*- coding: utf-8 -*-
__doc__="""
Opens the Info/ folder in ~/Library/Application support/Glyphs to update the GlyphsData.xml file.
"""

import subprocess

path = os.path.expanduser('~/Library/Application Support/Glyphs/Info')


print "Opening the Info/ folder: " + path


subprocess.call(["open", "-R", path])
