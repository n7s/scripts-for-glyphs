#MenuTitle: Update the preflight libraries from master
# -*- coding: utf-8 -*-
__doc__="""
Update the preflight libraries from master
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


preflightupdate = """

tell application "Finder"

	tell application "Terminal"

		activate

		tell window 1

			do script "sudo -H  /usr/local/bin/pip install --upgrade --user --no-warn-script-location git+https://github.com/silnrsi/pysilfont.git@master#egg=pysilfont git+https://github.com/googlei18n/glyphsLib.git@master#egg=glyphsLib git+https://github.com/fonttools/fonttools.git@master#egg=fontTools  git+https://github.com/LettError/MutatorMath.git@master#egg=MutatorMath  git+https://github.com/unified-font-object/ufoLib.git@master#egg=ufoLib git+https://github.com/typesupply/defcon.git@master#egg=defcon  git+https://github.com/typesupply/fontMath.git@master#egg=fontMath  git+https://github.com/LettError/DesignSpaceDocument.git@master#egg=DesignSpaceDocument "


		end tell

	end tell

end tell

tell application "Finder"
	display notification "Updating your preflight dependencies, please enter your user password" with title "Preflight dependencies update" sound name "default"
end tell


"""

save   = runAppleScript( preflightupdate )
