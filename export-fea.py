#MenuTitle: Export all features in .fea format
# -*- coding: utf-8 -*-
__doc__="""
Export all features in .fea format
"""

__copyright__ = 'Copyright (c) 2017, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger.'


# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

import os
import time

projectpath = Glyphs.font.filepath
sourceFolder = os.path.join(os.path.dirname(projectpath), '.')

print "\n# Path of source .glyphs file: " + projectpath

for font in Glyphs.fonts:
    print  "\n", "# Export of all OpenType features in .fea format for", Glyphs.font.familyName, " - version", Glyphs.font.versionMajor, ".", Glyphs.font.versionMinor, "on ", time.strftime('%Y-%m-%d-%H-%M'), "\n"


# first update all features
for feature in font.features:
        if feature.automatic:
                feature.update()

# access and output all features including prefixes
for feature in font.features:
    print feature.code

for prefix in font.featurePrefixes:
        print prefix.code


Glyphs.showNotification('Copy-n-paste between Start and End', 'Always check copyright and licensing')

# we still need a way to do the actual export beyond a copy-and-paste from the macro window
# and to save it in the appropriate folder structure
# filename = font.familyName + "-" + instance.weight + "-exported" + time.strftime('-%Y-%m-%d-%H-%M') + ".fea"
# Glyphs.showNotification('Exported OpenType code to ', filename, 'Check copyright and licensing before reusing any smart font code')
