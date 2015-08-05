# Aqui escribe tu codigo

import os
import sys
import urllib2
import re

class search_engine(object):
	"""docstring for ClassName"""
	def __init__(self):
		pass

	def menu(self):
		while True:
			self.clean_screen()
			self.menu_print()
			menu_option = self.menu_option()
			self.verify_option_menu(menu_option)
			self.menu_decision(menu_option)
		
	def menu_print(self):
		print "SEARCH WORD"
		print "EXIT"

	def menu_option(self):
		option_menu = raw_input("Type the option you want: ")
		option_menu = self.option_menu_min(option_menu)
		return option_menu

	#Function 1
	def option_menu_min(self, option_menu):
		option_menu = option_menu.lower()
		return option_menu

	#Function 2
	def verify_option_menu(self, option_menu):
		if option_menu == "search word" or option_menu == "exit":
			return "Valid option"
		else:
			return "Invalid option"

	def menu_decision(self, menu_option):
		if menu_option == "search word":
			self.option_search()
		elif menu_option == "exit":
			self.exit()
		else:
			message = raw_input("Invalid Input")

	def option_search(self):
		self.clean_screen()
		word, url1, url2 = self.ask_word_url()
		page_html1, page_html2 = self.open_page(url1, url2)
		count_page1 = self.count_page1(word, page_html1)
		count_page2 = self.count_page2(word, page_html2)
		more_repeated_word = self.more_repeated_word(word, count_page1, count_page2, url1, url2)

	def ask_word_url(self):
		word = raw_input("Type a word: ")
		url1 = raw_input("Type the first URL: ")
		url2 = raw_input("Type the second URL: ")
		return word, url1, url2

	def open_page(self, url1, url2):
		page1 = urllib2.urlopen(url1)
		page_html1 = page1.read()
		page2 = urllib2.urlopen(url2)
		page_html2 = page2.read()
		return page_html1, page_html2

	def search_word(self, word, page_html1, page_html2):
		if word in page_html1:
			count_page1 = self.count_page1(word, page_html1)
		if word in page_html2:
			count_page2 = self.count_page2(word, page_html2)
		return count_page1, count_page2

	def more_repeated_word(self, word, count_page1, count_page2, url1, url2):
		if count_page1 > count_page2:
			print "This is the URL that contains more the word: %s" % url1
		elif count_page2 > count_page1:
			print "This is the URL that contains more the word: %s" % url2
		message = raw_input("PRESS ENTER")

	#Function 3
	def count_page1(self, word, page_html1):
		count_page1 = page_html1.count(word)
		return count_page1

	#Function 4
	def count_page2(self, word, page_html2):
		count_page2 = page_html2.count(word)
		return count_page2

	def clean_screen(self):
		os.system('reset')

	def exit(self):
		self.clean_screen()
		sys.exit()

def my_application():
	my_program = search_engine()
	my_program.menu()

if __name__ == '__main__':
	my_application()
