#MenuTitle: Review helper: reveall all notes and annotations
# -*- coding: utf-8 -*-
__doc__="""
Review helper, see all annotations/notes in current font project, including selected ones
"""

__copyright__ = 'Copyright (c) 2017, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger.'



# brings macro window to front and clears its log:
Glyphs.clearLog()
Glyphs.showMacroWindow()

for font in Glyphs.fonts:
	for instance in font.instances:
			if instance.active:
				layer = Glyphs.font.selectedLayers[0] # current layer

print "\nNotes in", font.familyName, "font project: \n\n", font.note

print  "\nGlyphs annotations to review in selected layer :"
for annotation in layer.annotations:
	print layer, ":",  annotation.text

print  "\nGlyphs annotations to review across the whole font project :"
for glyph in font.glyphs:
			reviewable = glyph.name, ":", glyph.note
			print reviewable
			# still need to filter out the empty slots showing as None
