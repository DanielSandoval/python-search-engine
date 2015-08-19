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
		print "1.SEARCH WORD"
		print "2.EXIT"

	def menu_option(self):
		option_menu = raw_input("Type the number or option you want do: ")
		option_menu = self.option_menu_min(option_menu)
		return option_menu

	#Function 1
	def option_menu_min(self, option_menu):
		option_menu = option_menu.lower()
		return option_menu

	#Function 2
	def verify_option_menu(self, option_menu):
		if option_menu == "search word" or option_menu == "exit" or option_menu == "1" or option_menu == "2":
			return "Valid option"
		else:
			return "Invalid option"

	def menu_decision(self, menu_option):
		if menu_option == "search word" or menu_option == "1":
			self.option_search()
		elif menu_option == "exit" or menu_option == "2":
			self.exit()
		else:
			message = raw_input("Invalid Input")

	def option_search(self):
		self.clean_screen()
		verify_urls = "Incorrect urls"
		while verify_urls == "Incorrect urls":
			word, url1, url2 = self.ask_word_url()
			page_html1 = self.open_page1(url1)
			page_html2 = self.open_page2(url2)
			verify_urls = self.verify_urls(page_html1, page_html2)
		count_page1 = self.count_page1(word, page_html1)
		count_page2 = self.count_page2(word, page_html2)
		more_repeated_word = self.more_repeated_word(word, count_page1, count_page2, url1, url2)

	def ask_word_url(self):
		word = raw_input("Type a word: ")
		url1 = raw_input("Type the first URL: ")
		url2 = raw_input("Type the second URL: ")
		return word, url1, url2

	def open_page1(self, url1):
		try:
			page1 = urllib2.urlopen(url1)
			page_html1 = page1.read()
			return page_html1
		except:
			try:
				url1 = "http://%s" % url1
				page_html1 = self.open_page1(url1)
				return page_html1
			except:
				message = raw_input("You didn't type correctly the first URL")
				return "Incorrect url"

	def open_page2(self, url2):
		try:
			page2 = urllib2.urlopen(url2)
			page_html2 = page2.read()
			return page_html2
		except:
			try:
				url2 = "http://%s" % url2
				page_html2 = self.open_page2(url2)
				return page_html2
			except:
				message = raw_input("You didn't type correctly the second URL")
				return "Incorrect url"

	def verify_urls(self, page_html1, page_html2):
		if page_html1 == "Incorrect url" or page_html2 == "Incorrect url":
			verify_urls = "Incorrect urls"
			message = raw_input("You need type again the information!!!")
			self.clean_screen()
			return verify_urls
		else:
			return "Correct urls"

	#Function 3
	def count_page1(self, word, page_html1):
		count_page1 = page_html1.count(word)
		return count_page1

	#Function 4
	def count_page2(self, word, page_html2):
		count_page2 = page_html2.count(word)
		return count_page2

	def more_repeated_word(self, word, count_page1, count_page2, url1, url2):
		if count_page1 > count_page2:
			print "THIS IS THE URL THAT CONTAINS MORE THE WORD: ---> %s <--- APPEARS %s TIMES" % (url1, count_page1)
		elif count_page2 > count_page1:
			print "THIS IS THE URL THAT CONTAINS MORE THE WORD: ---> %s <--- APPEARS %s TIMES" % (url2, count_page2)
		elif count_page1 == count_page2 and count_page1 != 0 and count_page2 != 0:
			print "The word is repeated the same quatity of times in both pages"
		elif count_page1 == 0 and count_page2 == 0:
			print "The word you are searching is not in any page"
		message = raw_input("PRESS ENTER")

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
