#MenuTitle: Export all formats (.otf . ttf. .ufo .woff) to standard local folders
# -*- coding: utf-8 -*-
__doc__="""
Export all formats (.otf . ttf. .ufo .woff) to standard local folders
"""

__copyright__ = 'Copyright (c) 2017, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger.'

import os

projectpath = Glyphs.font.filepath
print "Path of current source file: " + projectpath

# Set build parameters
OTF_AutoHint = True
TTF_AutoHint = True
RemoveOverlap = True
UseSubroutines = True
UseProductionNames = True

# standard folders
buildFolder = os.path.join(os.path.dirname(projectpath), 'build')
sourceFolder = os.path.join(os.path.dirname(projectpath), 'source')
webFolder = os.path.join(os.path.dirname(projectpath), 'web')

# test standard subfolders are present, if not create them
try:
    os.makedirs(buildFolder),
except OSError:
    pass # already exists

try:
    os.makedirs(sourceFolder),
except OSError:
    pass # already exists

try:
    os.makedirs(webFolder),
except OSError:
    pass # already exists

# Export for all instances
for f in Glyphs.fonts:
    for instance in f.instances:
        if instance.active:
            result = instance.generate(FontPath=buildFolder)
            print  "\n", "Exporting all formats for", Glyphs.font.familyName, instance.weight, " - version",Glyphs.font.versionMajor,".",Glyphs.font.versionMinor

for instance in f.instances:
	instance.generate(Format = "OTF", FontPath = os.path.expanduser(buildFolder), AutoHint = OTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)

for instance in f.instances:
	instance.generate(Format = "TTF", FontPath = os.path.expanduser(buildFolder), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseProductionNames = UseProductionNames)

for instance in f.instances:
	ufoExporter = Glyphs.objectWithClassName_("GlyphsFileFormatUFO")
	ufoExporter.setConvertNames_(True)
	ufoExporter.setFontMaster_(font.masters[0])
	url = NSURL.fileURLWithPath_(sourceFolder + "/" + font.familyName + ".ufo")
	ufoExporter.writeUfo_toURL_error_(font, url, None)

for instance in f.instances:
	instance.generate(Format = "WOFF", FontPath = os.path.expanduser(webFolder), AutoHint = TTF_AutoHint, RemoveOverlap = RemoveOverlap, UseSubroutines = UseSubroutines, UseProductionNames = UseProductionNames)  #  WOFF export not ready yet (build 965)


Glyphs.showNotification('Exported formats to standard folders', '%s %s.%s\n%s' % (Glyphs.font.familyName, Glyphs.font.versionMajor, Glyphs.font.versionMinor, projectpath))
