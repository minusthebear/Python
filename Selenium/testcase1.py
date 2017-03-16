import os, sys, time, re, json
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class TestCase1(unittest.TestCase):

	def setUp(self):
		global driver
		chrome_path = "/Users/matthewhamann/chromedriver"
		driver = webdriver.Chrome(chrome_path)
		driver.get("http://travelingtony.weebly.com")

	def test_WaitForCheckOutPhotosButton(self):
		bLocator = "//span[.='Check out my coolest photos']"
		seebutton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bLocator)))

	def test_WaitForCheckOutInput(self):
		sLocator = "input.wsite-search-input"
		sField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sLocator)))

	def tearDown(self):
		driver.quit()

		
if __name__ == "__main__":
	unittest.main()