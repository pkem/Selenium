#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

valid_username = "xxxx"
valid_password = "xxxx"

class Logowanie_Wp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        #self.driver.implicitly_wait(10)

    def test_google(self):
        driver = self.driver
        driver.get("https://www.wp.pl")
        poczta = driver.find_element_by_link_text("POCZTA")
        poczta.click()
        logowanie = driver.find_element_by_id("login")
        logowanie.send_keys(valid_username)
        haslo = driver.find_element_by_id("password")
        haslo.send_keys(valid_password)
        driver.find_element_by_id("btnSubmit").click();
        folder = driver.find_element_by_link_text("Odebrane")
        folder.click()



    def tearDown(self):
        self.driver.find_element_by_link_text("wyloguj").click()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
