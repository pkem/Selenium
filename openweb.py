#!/usr/bin/env python

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://www.wsb.pl/wroclaw")
sleep(5)
driver.quit()
