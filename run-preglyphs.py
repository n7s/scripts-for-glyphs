#MenuTitle: Run preglyphs
# -*- coding: utf-8 -*-
__doc__="""
Runs preglyphs from your chosen project folder then open the generated file
"""

__copyright__ = 'Copyright (c) 2019, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

import GlyphsApp
from subprocess import Popen, PIPE


def runAppleScript(scpt, args=[]):
	p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(scpt)
	if stderr:
		print "AppleScript Error:"
		print stderr.decode('utf-8')
	return stdout


runpreglyphs = """

tell application "Finder"

	activate

	set frontmost to true

	set projectRoot to quoted form of POSIX path of (choose folder with prompt "Please select the project folder root, e.g. font-gentium")

	set sourcefolder to projectRoot & "source/"

	tell application "Terminal"

		activate

		tell window 1

			do script "cd " & projectRoot & "; ./preglyphs"

			delay 25

			do script "cd " & sourcefolder & "; open *.glyphs"

			tell window 1 to quit

		end tell

	end tell

end tell


"""

save   = runAppleScript( runpreglyphs )
