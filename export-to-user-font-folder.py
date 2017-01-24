#MenuTitle: Export all instances as OpenType to user font folder
# -*- coding: utf-8 -*-
__doc__="""
Export all instances as OpenType (.otf) to user font folder
"""

__copyright__ = 'Copyright (c) 2017, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger.'

path = os.path.expanduser('~/Library/Fonts')


for instance in Glyphs.font.instances:
        instance.generate(FontPath = exportFolder)

Glyphs.showNotification('Exporting OpenType fonts to user font folder', '%s %s.%s\n%s' % (Glyphs.font.familyName, Glyphs.font.versionMajor, Glyphs.font.versionMinor, path))
