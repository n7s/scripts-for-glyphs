#MenuTitle: Run preflightg - G for Glyphs -
# -*- coding: utf-8 -*-
__doc__="""
Runs the preflightg - G for Glyphs - shell script from your chosen project folder
"""

__copyright__ = 'Copyright (c) 2018, SIL International  (http://www.sil.org)'
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


runpreflightg = """

tell application "Finder"

	activate

	set frontmost to true

	set projectRoot to quoted form of POSIX path of (choose folder with prompt "Please select the project folder root, e.g. font-gentium" with invisibles)

	tell application "Terminal"

		activate

		tell window 1

			do script "cd " & projectRoot & "; ./preflightg"

		end tell

	end tell

end tell


tell application "Finder"
	display notification "Running preflightg on your project, watch for errors in the output, when done you can close the window" with title "Preflightg" sound name "default"
end tell



"""

save   = runAppleScript( runpreflightg )
