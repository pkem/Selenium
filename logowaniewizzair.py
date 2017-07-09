#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

imie = "aaa"
nazwisko = "bbbbbb"
invalid_email = "aaa.mail.com"

class Wizzair(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        #self.driver.implicitly_wait(10)


    def test_wizzair(self):
        driver = self.driver
        driver.get("https://wizzair.com/pl-pl/main-page#/")
        #uzycie selektor CSS
        logowanie_przycisk = driver.find_element_by_css_selector("#app > header > div > nav > ul > li:nth-child(3) > button")
        logowanie_przycisk.click()
        #uzycie selektor xpath, definiowanie wlasnych selektorow imie i nazwisko
        rejestracja_przycisk = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')
        rejestracja_przycisk.click()
        name = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name.send_keys(imie)
        lastname = driver.find_element_by_css_selector("input[placeholder=Nazwisko]")
        lastname.send_keys(nazwisko)

        #pisanie fragmentu JavaScriptu
        plec_wybor= driver.find_element_by_id("register-gender-male")
        driver.execute_script("arguments[0].click()", plec_wybor)
        wprowadz_numer = driver.find_element_by_css_selector("input[placeholder='Telefon komórkowy']")
        wprowadz_numer.send_keys("123456789")
        email_podaj = driver.find_element_by_css_selector("input[data-test=booking-register-email]")
        email_podaj.send_keys(invalid_email)
        haslo_podaj = driver.find_element_by_css_selector("input[data-test=booking-register-password]")
        haslo_podaj.send_keys("123hhhaaakks")
        country_field = driver.find_element_by_css_selector("input[data-test=booking-register-country]")
        country_field.click()
        kraj_wybor = driver.find_element_by_xpath('//*[@class="register-form__country-container__locations"]/label[164]')
        kraj_wybor.location_once_scrolled_into_view
        kraj_wybor.click()
        polityka_checkbox = driver.find_element_by_xpath('//*[@data-test="booking-register-privacy-policy"]')
        polityka_checkbox.click()
        zarejestruj_przycisk = driver.find_element_by_css_selector(
            ".button[type=submit][data-test=booking-register-submit]")
        self.assertFalse(zarejestruj_przycisk.is_enabled())
        #alarm nieprawidłowy adres email_podaj
        alarm_blednymail = driver.find_element_by_css_selector("div[class='error-notice error-notice--compact']")
        self.assertEqual(unicode(alarm_blednymail.text), u"Nieprawidłowy adres e-mail")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
