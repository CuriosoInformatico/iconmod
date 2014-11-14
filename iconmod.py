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


def main():
	os.system("clear")
	app_directory = '/usr/share/applications'

	print ("""
		Welcome to 

	 ___                __  __           _   _   ___  
	|_ _|___ ___  _ __ |  \/  | ___   __| | / | / _ \ 
	 | |/ __/ _ \| '_ \| |\/| |/ _ \ / _` | | || | | |
	 | | (_| (_) | | | | |  | | (_) | (_| | | || |_| |
	|___\___\___/|_| |_|_|  |_|\___/ \__,_| |_(_)___/ 
	                                                  

		""")
	print ("A Free OpenSource script by Curiosoinformatico.com\n\n")

	app = str(input("Write the name of the app: "))
	
	if not search_in_dir(app_directory, app):
		print ("The app"+app+"doesn't exist")
		quit()
	else:
		print ("\n\n--Here you have a search of the app--")

	print ("\n\n*   For security reasons   *\n\n")

	app_confirmed = str(input("Write the hole name of the file: "))
	
	if confirm(app_directory, app_confirmed):
		print ("APP Confirmed")
		img = tryopen()
		if img:
			change(app_confirmed,img)

	else:
		print ("APP no confirmada")


def search_in_dir(directory,app):
	isthere = False
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

def tryopen():
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

def change(app,img):
	try:
		f = open('/usr/share/applications/' + app,'rt')
		lines = f.read().split('\n')
		f.close()
		
		new_file = ""
		for line in lines:
			if 'Icon' in line:
				line = 'Icon=' + img
				print (line)
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
			print ("Wops! Something Fails...")
			print ("It seems like u dont hace permissions")
			input ("Press ENTER to end and try to execute with sudo")

	except:
		print ("ERROR")


main()
quit()