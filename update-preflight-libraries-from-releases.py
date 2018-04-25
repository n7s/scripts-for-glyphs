#MenuTitle: Update the preflight libraries from releases
# -*- coding: utf-8 -*-
__doc__="""
Update the preflight libraries from releases
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

			do script "sudo -H  /usr/local/bin/pip install --disable-pip-version-check --upgrade --user git+https://github.com/silnrsi/pysilfont.git@v1.3.0#egg=pysilfont;  sudo -H  /usr/local/bin/pip install --disable-pip-version-check --upgrade --user glyphsLib;  sudo -H  /usr/local/bin/pip  install --disable-pip-version-check  --upgrade --user fontTools ;  sudo -H  /usr/local/bin/pip install --disable-pip-version-check  --upgrade --user MutatorMath ;  sudo -H  /usr/local/bin/pip  install --disable-pip-version-check  --upgrade --user ufoLib ;  sudo -H  /usr/local/bin/pip install --disable-pip-version-check --upgrade  --user defcon ;  sudo -H  /usr/local/bin/pip install --disable-pip-version-check  --upgrade --user fontMath ;  pip list --format=columns --disable-pip-version-check --pre"

		end tell

	end tell

end tell


"""

save   = runAppleScript( preflightupdate )
