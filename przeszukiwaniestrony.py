#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

"""
Get „http://wp.pl” startpage
Check if there is a specific word
Check if more that one
"""

szukane_slowo = "Sport"
class SzukajstronaWP(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def wyszukajslowa(self):
        self.driver.get("http://www.wp.pl")
        driver = self.driver
        esults = driver.find_elements_by_xpath('//div[contains(text(), "' + search_word + '")]')
        print(len(results))
        self.assertGreaterEqual(len(results), 1)

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity=2)
