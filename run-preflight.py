#MenuTitle: Run preflight (from your project folder)
# -*- coding: utf-8 -*-
__doc__="""
Runs the preflight shell script from your chosen project folder
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


runpreflight = """

tell application "Finder"

	set projectRoot to (quoted form of POSIX path of (choose folder))

	tell application "Terminal"

		activate

		tell window 1

			do script "cd " & projectRoot & "; ./preflight"

		end tell

	end tell

end tell


"""

save   = runAppleScript( runpreflight )
