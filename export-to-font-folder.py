#MenuTitle: Export all instances as OpenType to user font folder
# -*- coding: utf-8 -*-
__doc__="""
Export all instances as OpenType (.otf) to user font folder
"""

path = os.path.expanduser('~/Library/Fonts')


for instance in Glyphs.font.instances:
        instance.generate(FontPath = path)

Glyphs.showNotification('Exporting OpenType fonts to user font folder', '%s %s.%s\n%s' % (Glyphs.font.familyName, Glyphs.font.versionMajor, Glyphs.font.versionMinor, path))
