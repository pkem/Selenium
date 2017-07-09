# -*- coding: utf-8" -*
import unittest
from selenium import webdriver

"""
Get „http://wp.pl” startpage
Check if there is a specific word
Check if more that one
"""


search_word = "Skoki"

class WpPlSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        self.driver.get("http://www.wp.pl")
        results = self.driver.find_elements_by_xpath('//div[contains(text(), "' + search_word + '")]')
        print(len(results))
        self.assertGreaterEqual(len(results), 1)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
