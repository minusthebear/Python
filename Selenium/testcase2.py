import os, sys, time, re, json
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest


class TestCase2(unittest.TestCase):

	def setUp(self):
		global driver
		chrome_path = "/Users/matthewhamann/chromedriver"
		driver = webdriver.Chrome(chrome_path)
		driver.get("http://travelingtony.weebly.com")

	def test_AssertTitle(self):
		self.assertEqual(driver.title, "Traveling Tony's Photography - Welcome")

	def test_AssertNotTitle(self):
		self.assertNotEqual(driver.title, "Traveling John's Photography - Welcome")

	def tearDown(self):
		driver.quit()

		
if __name__ == "__main__":
	unittest.main()