#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Google_check(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        #self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://google.pl")
        enter = driver.find_element_by_id("lst-ib")
        enter.send_keys("tester")
        enter.submit()
        results = WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME,"g")))
        print (str(len(results)))
        for result in results:
            print (result.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
