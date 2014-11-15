#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""

Created by Samuel López Saura
@E-mail: samuellopezsaura@gmail.com
@Web Page: http://www.blog.curiosoinformatico.com
@Twitter: @Mago_Geminis

Just for fun.

"""


import os
import errors

def main():
	os.system("clear")
	app_directory = '/usr/share/applications'

	print ("""
		Welcome to 

	 ___                __  __           _   _   _ 
	|_ _|___ ___  _ __ |  \/  | ___   __| | / | / |
	 | |/ __/ _ \| '_ \| |\/| |/ _ \ / _` | | | | |
	 | | (_| (_) | | | | |  | | (_) | (_| | | |_| |
	|___\___\___/|_| |_|_|  |_|\___/ \__,_| |_(_)_|
	                                               
		""")
	print ("A Free OpenSource script by Curiosoinformatico.com\n\n")

	app = str(input("Write the name of the app: "))
	
	if not search_in_dir(app_directory, app):
		errors.noApp()
	else:
		print ("\n\n*   For security reasons   *\n\n")

		app_confirmed = str(input("Write the hole name of the file: "))
		
		if confirm(app_directory, app_confirmed):
			print ("APP Confirmed")
			img = tryopen()
			if img: # If the image exist
				if copyimg(img): # If the program can copy the image
					name = getName(img) # Get the name of the image
					change(app_confirmed,"/opt/iconmod/photos/"+name) # Change the files
				else:
					errors.permissionError()

		else:
			print ("Wrong APP name")
			input("Press Enter to end")


def search_in_dir(directory,app):
	isthere = False
	print ("\n\n"+"*"*30+"\nApps with that name:\n\n")
	for ele in os.listdir(directory):
		if app in ele:
			isthere = True
			print (ele)
		else:
			pass

	return isthere


def confirm(directory, data_confirmed):
	for ele in os.listdir(directory):
		if data_confirmed == ele:
			return True
		else:
			pass	
	return False

def tryopen(): # Try verify if the image exists
	img = str(input("Write please the path of the image: "))
	try:
		open(img,'rb').close()
		print ('Path confirmed')
		return img
	except:
		while True:
			print('Error on the path')
			print ('Try another path?[y][n]')
			x = str(input('    >>'))
			if x == 'y' or x == 'Y':
				tryopen()
				return img
			elif x == 'n' or x == 'N':
				return False
			else:
				pass

def getName(img):
	path = img.split("/")
	name = path[-1]
	return name

def copyimg(img): # Try to copy the image
	name = getName(img)

	try:
		f_origin = open(img,"rb")
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
		f = open('/usr/share/applications/' + app,'rt')
		lines = f.read().split('\n')
		f.close()
		
		new_file = ""
		for line in lines:
			if 'Icon' in line:
				line = 'Icon=' + img
			else:
				pass
			new_file += line + '\n'
		 	
		try:
			f = open('/usr/share/applications/' + app,'wt')
			f.write(new_file)
			f.close()
			print ("\n\nAll Done my friend! :D!")
			input ("\n\nPress Enter to finalize")
		except:
			errors.permissionError()

	except:
		print ("ERROR")


main()
