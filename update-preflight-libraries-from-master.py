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

			do script "sudo -H  /usr/local/bin/pip install --upgrade --user  git+https://github.com/silnrsi/pysilfont.git@master#egg=pysilfont;  sudo -H  /usr/local/bin/pip install --upgrade --user git+https://github.com/googlei18n/glyphsLib.git@master#egg=glyphsLib;  sudo -H  /usr/local/bin/pip install  --upgrade --user git+https://github.com/fonttools/fonttools.git@master#egg=fontTools ;  sudo -H  /usr/local/bin/pip install  --upgrade --user git+https://github.com/LettError/MutatorMath.git@master#egg=MutatorMath ;  sudo -H  /usr/local/bin/pip install  --upgrade --user git+https://github.com/unified-font-object/ufoLib.git@master#egg=ufoLib ;  sudo -H  /usr/local/bin/pip install --upgrade  --user git+https://github.com/typesupply/defcon.git@master#egg=defcon ;  sudo -H  /usr/local/bin/pip install  --upgrade --user git+https://github.com/typesupply/fontMath.git@master#egg=fontMath "

		end tell

	end tell

end tell


"""

save   = runAppleScript( preflightupdate )
