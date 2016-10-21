#MenuTitle: Smith helper (font production toolchain)
# -*- coding: utf-8 -*-
__doc__="""
Launch smith (with vagrant underneath) with output in the Macro Window.
a.k.a a big button for the blackbox.
"""

__copyright__ = 'Copyright (c) 2016, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger.'

# you need the vanilla, vagrant and fabric python modules 

import vanilla, subprocess, os, sys, vagrant
from fabric.api import env, execute, task, run

# expanding the path to see vagrant and virtualbox binaries from Glyphs
os.environ["PATH"] = os.environ["PATH"] + ":/opt/vagrant/bin" + ":/Applications/VirtualBox.app/Contents/MacOS"


class SmithLaunch( object ):
	def __init__( self ):
		# Window 'self.w':
		windowWidth  = 700
		windowHeight = 500
		windowWidthResize  = 900 # user can resize width by this value
		windowHeightResize = 900 # user can resize height by this value
		self.w = vanilla.FloatingWindow(
			( windowWidth, windowHeight ), # default window size
			"Smith helper: black button on a black panel of the blackbox that lights up black when it's done", # window title
			minSize = ( windowWidth, windowHeight ), # minimum size (for resizing)
			maxSize = ( windowWidth + windowWidthResize, windowHeight + windowHeightResize ), # maximum size (for resizing)
			autosaveName = "org.sil.scripts.smith.mainwindow" # stores last window position and size
		)

		# UI elements:
		self.w.descriptionText = vanilla.TextBox( (55-1, 12+2, -54, 14), "Add the full path (with final /) for each smith-enabled project repository (1 per line):", sizeStyle='small' )
		self.w.ProjectPaths = vanilla.TextEditor( (15, 12+20, -55, -40),
			text="/Users/johndoe/projects/font-example/",
		)

		# Run Button:
		self.w.runButton = vanilla.Button((-175, -20-15, -15, -15), "Launch smith [%]", sizeStyle='regular', callback=self.SmithLaunchMain )
		self.w.setDefaultButton( self.w.runButton )

		# Load Settings:
		if not self.LoadPreferences():
			print "Note: 'Smith helper' could not load project preferences. Will resort to defaults"

		# Open window and focus on it:
		self.w.open()
		self.w.makeKey()

	def SavePreferences( self, sender ):
		try:
			Glyphs.defaults["org.sil.scripts.smith.ProjectPaths"] = self.w.ProjectPaths.get()
		except:
			return False

		return True

	def LoadPreferences( self ):
		try:
			NSUserDefaults.standardUserDefaults().registerDefaults_(
				{
					"org.sil.scripts.smith.ProjectPaths": "/Users/johndoe/projects/font-example/"
				}
			)
			self.w.ProjectPaths.set( Glyphs.defaults["org.sil.scripts.smith.ProjectPaths"] )
		except:
			return False

		return True

	def SmithLaunchMain( self, sender ):
		try:
			# brings macro window to front and clears its log:
			Glyphs.clearLog()
			Glyphs.showMacroWindow()

			paths = self.w.ProjectPaths.get().splitlines()
			for thisPath in paths:
				thisPath = thisPath.strip()
				if thisPath:
					lineLength = len(thisPath)

					# put in your path manually if you need to:
					# os.chdir('/Users/johndoe/projects/font-example/')

					os.chdir( thisPath )

					@task
					def mytask():
						run('cd /smith/ && smith distclean && smith configure && smith build && smith pdfs && smith xtest && smith zip && smith srcdist')

					v = vagrant.Vagrant(quiet_stdout=False, quiet_stderr=False)

					# log_cm = vagrant.make_file_cm('deployment.log')
					# v = vagrant.Vagrant(out_cm=log_cm, err_cm=log_cm)

					v.up()
					v.provision()
					v.status()
					env.hosts = [v.user_hostname_port()]
					env.key_filename = v.keyfile()
					env.disable_known_hosts = True # useful for when the vagrant box ip changes.
					execute(mytask) # run a fabric task on the vagrant host.

					print "\n%s\n%s\n%s\n Smith helper output (0=OK): " % ( "-"*lineLength, thisPath, "-"*lineLength )

					print """
					Done. Your smith build is complete.
					Extra targets have also been run. You will find the generated files in the results/ folder.
					"""


					print "Opening the results/ folder:"

					subprocess.call(["open", "-R", 'results'])

					Glyphs.showMacroWindow()


			if not self.SavePreferences( self ):
				print "Note: 'Smith helper could not write project preferences."

		except Exception, e:
			# brings macro window to front and reports error:
			Glyphs.showMacroWindow()
			print "Smith helper error: %s" % e

SmithLaunch()



