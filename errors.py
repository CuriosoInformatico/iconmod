#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def pause():
	input("Press ENTER to finalize")

def permissionError():
	print ("Wops!\nIt seems like u dont have permissions to do that")
	pause()
	quit()

def noApp():
	print ("Hey!\nI think you write wrong the name of the App")
	pause()