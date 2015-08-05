import application
import unittest

class Test_Search_Engine(unittest.TestCase):
	"""docstring for Test_Search_Engine"""
	#Function 1: option_menu_min
	def test_option_menu_min(self):
		class_application = application.search_engine()
		self.assertTrue(class_application.option_menu_min("SEARCH").islower())
	#Function 2: verify_option_menu
	def test_verify_option_menu(self):
		class_application = application.search_engine()
		self.assertEqual(class_application.verify_option_menu("search word"), "Valid option")
		self.assertEqual(class_application.verify_option_menu("HOLA"), "Invalid option")
	#Function 3: count_page1
	def test_count_page1(self):
		class_application = application.search_engine()
		self.assertTrue(type(class_application.count_page1("Python", "https://es.wikipedia.org/wiki/Python")) == int)
	#Function 3: count_page2
	def test_count_page2(self):
		class_application = application.search_engine()
		self.assertTrue(type(class_application.count_page2("Python", "https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n")) == int)

if __name__ == '__main__':
	unittest.main()
		