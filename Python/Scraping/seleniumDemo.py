import os, sys, time, re, json
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import *

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True


class DriverDemo:

	def __init__(self):
		self.startDriver()

	def startDriver(self):
		chrome_path = "/Users/matthewhamann/chromedriver"
		driver = webdriver.Chrome(chrome_path)
		driver.get("http://stackoverflow.com")

		driver2 = webdriver.Firefox(capabilities=firefox_capabilities)
		driver2.get("http://wired.com")

		
if __name__ == "__main__":

	DriverDemo()