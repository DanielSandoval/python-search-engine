# Aqui escribe tu codigo

import os
import sys
import urllib2
import re

def ask_word_url():
	word = raw_input("Type a word: ")
	url1 = raw_input("Type the first URL: ")
	url2 = raw_input("Type the second URL: ")

def clean_screen():
	os.system('reset')

def exit():
	sys.exit()

def my_application():
		clean_screen()
		ask_word_url()
		exit()

my_application()
