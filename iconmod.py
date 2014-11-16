#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#########################################################################
# IconMod is a Script made in Python3 which gives us the option         #
# of changing the icons of our programs quickly, safely and accurately. #
#########################################################################
 


"""

Created by Samuel López Saura
@E-mail: samuellopezsaura@gmail.com
@Web Page: http://www.blog.curiosoinformatico.com
@Twitter: @Mago_Geminis

Just for fun.

Helped by Fanta (get the idea for the 1.2 from here):
        http://pastebin.com/RwDCPGDi
       For Fanta: Gracias por ayudar :)

"""


# Modules
import sys
import os
import errors


# Variables
APP_NAME = 'IconMod'
VERSION = 1.2
APP_DIRECTORY = '/usr/share/applications/'
HELP = """
-s | --search \t\tSearch an application
------------------------------------------------
-i | --icon    \t\tSearch    an    icon
------------------------------------------------
-v | --version \t\tShow	 the  version
------------------------------------------------
-g | --guided \t\tGuided           mode
------------------------------------------------
-h | --help   \t\tShow    this     help
------------------------------------------------

Example of use to change an icon:
iconmod -s firefox -i /home/user/downloads/icon.png
"""
# Code :)

def main():
	os.system("clear")
	if sys.version_info<(3,1,4):
		errors.lowVersion()
	else:
		# If no parameters...
		if len(sys.argv) == 1:
			print(APP_NAME, VERSION, "\n" + HELP)

		# In the case of 1 parameter...
		elif len(sys.argv) == 2:
			if sys.argv[1] == "-h" or sys.argv[1] == "--help":
				print(APP_NAME, VERSION + "\n" + HELP)
			elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
				print(nombre, version)
			elif sys.argv[1] == "-s" or sys.argv[1] == "--search":
				errors.missingError('name')
			elif sys.argv[1] == "-g" or sys.argv[1] == "--guided":
				guidedMode()

		# In the case of 2 parameters...
		elif len(sys.argv) == 3:
			if sys.argv[1] == "-s" or sys.argv[1] == "--search":
				app = sys.argv[2]
			if not searchInDir(app,False):
				errors.noApp()
				exit(1)
			else:
				errors.missingError('icon')

		# In the case of 3 parameters...
		elif len(sys.argv) == 4:
			if sys.argv[1] == "-s" or sys.argv[1] == "--search" and sys.argv[3] == "-i" or sys.argv[3] == "--icon":
				errors.missingError('icon')

		# In the case of 4 parameters...
		elif len(sys.argv) == 5:
			if sys.argv[1] == "-s" or sys.argv[1] == "--search" and sys.argv[3] == "-i" or sys.argv[3] == "--icon":
				app = sys.argv[2]
				img = sys.argv[4]

				if not searchInDir(app,False):
					errors.noApp()
				else:
					app_confirmed = (app + ".desktop")

				if confirm(app_confirmed):
					if tryopen(False):
						name = getFullName(img,app_confirmed) # Name of the photo in  /opt/photos/
						if copyimg(img, name): # If the program can copy the image
							change(app_confirmed,"/opt/iconmod/photos/"+name) # Change the files
				else:
					errors.noApp()


# Guided mode. A mode were the IconMod is asking for parameters
# Specially usefull when a aplication have more than one name
# or we dont know exactly how its named the file of the aplication

def guidedMode():
	print ("""
		Welcome to 
	 ___                __  __           _   _   ____  
	|_ _|___ ___  _ __ |  \/  | ___   __| | / | |___ \ 
	 | |/ __/ _ \| '_ \| |\/| |/ _ \ / _` | | |   __) |
	 | | (_| (_) | | | | |  | | (_) | (_| | | |_ / __/ 
	|___\___\___/|_| |_|_|  |_|\___/ \__,_| |_(_)_____|
	                                                   

		""")
	print ("A Free OpenSource script by Curiosoinformatico.com\n\n")

	app = str(input("Write the name of the app: "))
	
	if not searchInDir(app,True):
		errors.noApp()
	else:
		print ("\n\n*   For security reasons   *\n\n")

		app_confirmed = str(input("Write the hole name of the file: "))
		

		if confirm(app_confirmed):
			print ("APP Confirmed")
			img = tryopen(True)
			if img: # If the image exist
				name = getFullName(img,app_confirmed) # Name of the photo in  /opt/photos/
				if copyimg(img, name): # If the program can copy the image
					change(app_confirmed,"/opt/iconmod/photos/"+name) # Change the files
				else:
					errors.permissionError()

		else:
			errors.noApp()


# Usefull functions
def searchInDir(app,verbose):
	isthere = False
	that_name = []
	for ele in os.listdir(APP_DIRECTORY):
		if app in ele:
			isthere = True
			that_name.append(ele)
		else:
			pass

	if verbose:
		print ("\n\n"+"*"*30+"\nApps with that name:\n\n")
		for ele in that_name:
			print (ele)

	return isthere


def confirm(data_confirmed):
	for ele in os.listdir(APP_DIRECTORY):
		if data_confirmed == ele:
			return True
		else:
			pass	
	return False

def tryopen(verbose): # Try to verify if the image exists
	if verbose:
		img = str(input("Write please the path of the image: "))
	else:
		img = sys.argv[4]
	try:
		open(img,'rb').close()
		print ('Path confirmed')
		return img
	except:
		if verbose:
			while True:
				print('Error on the path')
				print ('Try another path?[y][n]')
				x = str(input('    >>'))
				if x == 'y' or x == 'Y':
					tryopen(True)
					return img
				elif x == 'n' or x == 'N':
					return False
				else:
					pass
		else:
			errors.noImg()

def getName(img): # Get the last Item of a path
	path = img.split("/")
	name = path[-1]
	return name

def getFullName(img, app_name): # Return the appname.extensionimg
	img_name = getName(img)
	print (img_name)
	print (app_name)
	return app_name.split(".")[0]+"."+img_name.split(".")[1]

def copyimg(img, name): # Try to copy the image
	print ("Open: "+img)
	print (name)
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
		f = open(APP_DIRECTORY + app,'rt')
		lines = f.read().split('\n')
		f.close()
		
		new_file = ""
		for line in lines:
			line_s = line.split("=")
			if line_s[0] == 'Icon':
				line = 'Icon='+img
			else:
				pass
			if line != "":
				new_file += line + '\n'
		 	
		f = open(APP_DIRECTORY + app,'wt')
		f.write(new_file)
		f.close()
		print ("\n\nAll Done my friend! :D!")
		errors.pause()

	except:
		errors.permissionError()

# End of the Script ##

# Call to main function
if __name__ == "__main__":
	main()