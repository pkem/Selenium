#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep

class WsbPlCheck(unittest.TestCase):
#warunki wstepne setUp
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  #czeka maksymalnie 10 sekund chyba ze uda sie szybciej wykonac
#test - wykonanie samego testu
    def test_cos(self):
        driver = self.driver
        driver.get("http://www.wsb.pl/wroclaw")
        self.assertIn("WSB Wrocław".decode("utf-8"),driver.title)
        #driver.find_element_by_id("edit-search-block-form--2")
        #driver.find_element_by_name("search_block_form")
        #tworzenie obiektu
        #podyplomowe_link = driver.find_element_by_link_text("Studia podyplomowe")
        #podyplomowe_link.click()

        search_box = driver.find_element_by_id("edit-search-block-form--2")
        search_box.send_keys("tester")
        search_box.submit()
        results = driver.find_elements_by_class_name("search-result")

        print ("Znalazlem "+ str(len(results)) + "Wynikow na tej stronie: \n")

        for result in results:
            print(result.text +"\n")
        self.assertEqual(10, len(results))

        #driver.find_element_by_partial_link_text("MBA")
    def test_google(self):
        driver = self.driver
        driver.get("http://www.google.pl")
        driver.find_element_by_id("lst-ib")

#to co sie bedzie robilo po tescie
    def tearDown(self):
        self.driver.quit()
#parametr verbosity wymusza wiecej szczegolow testow
if  __name__ == "__main__":
    unittest.main(verbosity=2)
