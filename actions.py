#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
In this file we have functions that controls the behaviour
of the app.
"""

import do
import errors

def changeAppLocalIcon(app, img):
	if do.confirm(app):
		if do.tryOpen(img): 
			name = do.getFullName(img,app) # Name of the photo in  /opt/photos/
			if do.copyImg(img, name): # If the program can copy the image

				if (do.change(app,"/opt/iconmod/photos/" + name)):
					print ("\n\nAll Done my friend! :D!")
					errors.pause()
				else:
					errors.permissionError()

			else:
				print ("\n")
				errors.permissionError()

def changeAppNetworkIcon(app, url):
	if do.confirm(app):
		name = do.getFullName(url, app)
		if do.downloadImg(name,url):
			print ("Image downloaded")

			if (do.change(app,"/opt/iconmod/photos/"+name)):
				print ("\n\nAll Done my friend! :D!")
				errors.pause()
			else:
				errors.permissionError()

		else:
			errors.wrongUrl()