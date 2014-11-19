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

Actual Version is a 1.3 BETA

Help to develop here: github.com/curiosoinformatico/iconmod
"""


# Modules
import sys
import os
import errors
import actions


# Variables
APP_NAME = 'IconMod'
VERSION = 1.2
APP_DIRECTORY = '/usr/share/applications/'
HELP = """
-s | --search \t\tSearch an application
------------------------------------------------
-u | --url    \t\tGet the image from the network
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
------------------------------------------------
|-iconmod -s firefox -i /home/user/downloads/icon.png
|-iconmod -s firefox -u https://www.debian.org/Pics/openlogo-50.png

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
				print(APP_NAME, VERSION , "\n" + HELP)
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
			if not searchInDir(app, False):
				errors.noApp()
				exit(1)
			else:
				errors.missingError('icon')

		# In the case of 3 parameters...
		elif len(sys.argv) == 4:
			if sys.argv[1] == "-s" or sys.argv[1] == "--search" and sys.argv[3] == "-i" or sys.argv[3] == "--icon":
				errors.missingError('path')


################################(-- When the magic happens --)##########################################################


		# In the case of 4 parameters...
		elif len(sys.argv) == 5:

			app = sys.argv[2]
			img = sys.argv[4]
			
			if not searchInDir(app, False):
				errors.noApp()
				quit()
			else:
				app_confirmed = (app + ".desktop")

			# Local Image			
			if (sys.argv[1] == "-s" or sys.argv[1] == "--search") and (sys.argv[3] == "-i" or sys.argv[3] == "--icon"):
				actions.changeAppLocalIcon(app_confirmed,img)

			# Image on the network
			elif (sys.argv[1] == "-s" or sys.argv[1] == "--search") and (sys.argv[3] == "-u" or sys.argv[3] == "--url"):
				actions.changeAppNetworkIcon(app_confirmed,img)

			else:
				errors.wrongArgs()

		else:
			errors.wrongArgs()


# Guided mode. A mode were the IconMod is asking for parameters
# Specially usefull when a aplication have more than one name
# or we dont know exactly how its named the file of the aplication

def guidedMode():
	print ("""
		Welcome to 

	 ___                __  __           _   _   _____ 
	|_ _|___ ___  _ __ |  \/  | ___   __| | / | |___ / 
	 | |/ __/ _ \| '_ \| |\/| |/ _ \ / _` | | |   |_ \ 
	 | | (_| (_) | | | | |  | | (_) | (_| | | |_ ___) |
	|___\___\___/|_| |_|_|  |_|\___/ \__,_| |_(_)____/ 
	                                                   
				  Beta... just testing  :D

		""")
	print ("A Free OpenSource script by Curiosoinformatico.com\n\n")

	app = str(input("Write the name of the app: "))
	
	if not searchInDir(app, True):
		errors.noApp()
	else:
		print ("\n\n*   For security reasons   *\n\n")
		app_confirmed = str(input("Write the hole name of the file: ")).strip()
		place = str(input("Is the image local or on the Network? [L][n]")).strip()
		
		if place == 'n' or place == 'N':
			url = str(input("Write the URL of the image: ")).strip()
			actions.changeAppNetworkIcon(app_confirmed,url)
		else:
			img = str(input("Write the hole path of the image: ")).strip()
			actions.changeAppLocalIcon(app_confirmed,img)

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

# End of the Script ##

# Call to main function
if __name__ == "__main__":
	main()