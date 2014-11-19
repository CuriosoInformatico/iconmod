#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
About this file:
	Here are the error notifications.
	
	missingError is a function for the Errors where
	an argument is missing.
		It can be: 
			'name' >> name of the App
			'icon' >> path of the icon


"""


def pause():
	input("Press ENTER to finalize")

def lowVersion():
	print("\nERROR: You need at least Python 3.1.4 to run this Script\n\n\n")

def permissionError():
	print ("Wops!\nIt seems like u dont have permissions to do that")
	pause()
	exit(1)

def noApp():
	print ("Hey!\nI think you write wrong the name of the App")
	pause()


def noImg():
	print ("Hey!\nI think you write wrong the path of the image")
	pause()

def wrongUrl():
	print ("Hey!\nIt seems like you bring a link that is broke")
	pause()
	exit(1)

def wrongArgs():
	print ("Hey!\nYou write wrong the arguments... Try iconmod --help")
	pause()
	quit()

def wrongFormat():
	print ("Hey!\nIt seems like you write wrong something.")
	print ("See the doc on https://github.com/CuriosoInformatico/iconmod/wiki")
	pause()
	quit()

def missingError(miss):
	if miss == 'name':
		print("Missing the name of the application\n")
	elif miss == 'icon':
		print("Missing Icon: \nAdd the -i parameter to specify the path of the image\n")
	elif miss == 'path':
		print("Missing Icon: \nYou need to add the path of the image\n")
