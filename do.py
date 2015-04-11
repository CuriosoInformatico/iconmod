#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import errors
import urllib.request
from configparser import ConfigParser

# Usefull functions
APP_DIRECTORY = '/usr/share/applications/'

def confirm(data_confirmed, place = APP_DIRECTORY): 
	# Try to confirm if something is in the directory
	for ele in os.listdir(place):
		if data_confirmed == ele:
			return True
		else:
			pass	
	return False

def tryOpen(img): # Try to verify if the image exists
	try:
		open(img,'rb').close()
		print ('Path confirmed')
		return img
	except:
			errors.noImg()

def getName(img): # Get the last Item of a path
	path = img.split("/")
	name = path[-1]
	return name

def getFullName(img, app_name): # Return the appname.extensionimg
	try:
		img_name = getName(img)
		print (img_name)
		print (app_name)
		return app_name.split(".")[0]+"."+img_name.split(".")[1]
	except:
		errors.wrongFormat()

def downloadImg(img_name, url): # Download the image
	if confirm (img_name, '/opt/iconmod/photos/'):
		os.remove('/opt/iconmod/photos/' + img_name)
	try:
		img = "/opt/iconmod/photos/" + img_name
		urllib.request.urlretrieve(url, img)
		return True
	except:
		return False

def copyImg(img, name): # Try to copy the image
	print ("Open: "+img)
	print (name)
	try:
		f_origin = open(img, "rb")
		r = f_origin.read()
		f_origin.close()

		f_destiny = open("/opt/iconmod/photos/"+name, "wb")
		w = f_destiny.write(r)
		f_destiny.close()
		return True
	except:
		return False


def change(app,img):
	try:
		fullPath = APP_DIRECTORY + app
		config = ConfigParser()
		config.optionxform = str # case sensitive
		config.read(fullPath)
		config['Desktop Entry']['Icon'] = img
		with open(fullPath, 'wt') as fich:
			config.write(fich)
			print ('Already done! File modified: '+ fullPath)
		return True
	except:
		return False