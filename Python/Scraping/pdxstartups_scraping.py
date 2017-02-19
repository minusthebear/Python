# selenium-2.53.6
import os, sys, time, re, json
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class fullFunc:

	def __init__(self, outfile):
		self.quit = None
		self.foundIt = None
		self.outfile = outfile
		self.arr = multiprocessing.Manager().list()
		self.scrapeAllPages()

	def foo(self, n):
		while not self.quit.is_set():
			for i in range(n):
				time.sleep(1)
			self.foundIt.set()
			self.quit.set()

	def bigArray(self, val):
		self.arr.append(val)
		
	def retValues(self, ID, title, location, datePublished, languages, link):
		loop = "["
		length = len(languages)
		num = 0
		for l in languages:
			loop = loop + "\"" + l + "\""
			num = num + 1
			if (num < length):
				loop = loop + ", "
		loop = loop + "]"
		string = "{\"id\": " + ID + ", \"title\": \"" + title + "\", \"location\": \"" + location + "\", \"date\": \"" + datePublished + "\", \"languages\": " + loop + ", \"link\": \"" + link + "\"}"
		return string

	def doJSON(self, driver, length, a, i):
		x = self.setUpJSON(driver, length, a, i)
		self.bigArray(x)
		self.foundIt.set()


	def setUpJSON(self, driver, length, a, i):

		ID = ""
		title = ""
		location = ""
		datePublished = ""
		link = ""
		languages = []

		while not self.quit.is_set():

			l = a.find_element_by_class_name("post-list-content")
			m = l.find_element_by_tag_name("a")

			# Open the link in a new tab by sending key strokes on the element
			n = m.send_keys(Keys.COMMAND + Keys.RETURN) # Should be Keys.CONTROL on Windows
			
			# Switch tab to the new tab, which we will assume is the next one on the right
			driver.find_element_by_tag_name("body").send_keys(Keys.COMMAND + Keys.TAB)
			driver.switch_to_window(driver.window_handles[1])

			link = driver.current_url
			ID = link.split('/')[-1]

			try:
				element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "post-title")))
				title = driver.find_element_by_class_name("post-title").text.strip()
			except:
				print("Not Found title")

			try:
				element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='post-body-meta']")))
				city = driver.find_elements_by_xpath("//div[@class='post-body-meta']/span[1]/a")[0].text.strip()
				lan = driver.find_elements_by_xpath("//div[@class='post-body-meta']/span[2]/a")
				for l in lan:
					languages.append(l.text.strip())
			except:
				print("Not Found city/languages")	

			try:
				element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "main_post")))
				datePublished = driver.find_elements_by_class_name("js-post-meta")[0].text.strip().split(' on ')[-1]
			except:
				print("Not Found")

			try:
				x = self.retValues(ID, title, location, datePublished, languages, link)
				return x
			except:
				pass
			return

	def scrapeAllPages(self):
		chrome_path = "/Users/matthewhamann/chromedriver"
		driver = webdriver.Chrome(chrome_path)

		self.outfile.write("{\n")

		driver.get("https://pdxstartups.switchboardhq.com/?page=1") 
		self.scrapeAllTabs(driver)

		i = 0
		for a in self.arr:
			length = len(self.arr)
			self.outfile.write("\"" + str(i) + "\":")
			json.dump(a, self.outfile)
			i = i + 1
			if (i < length):
				self.outfile.write(",\n")

		self.outfile.write("}")
		driver.quit()


	def scrapeAllTabs(self, driver):

		i = 1
		main_window = driver.current_window_handle

		ask_tabs = driver.find_elements_by_class_name("post-list-item-ask")
		length = len(ask_tabs)

		for a in ask_tabs:
			self.quit = multiprocessing.Event()
			self.foundIt = multiprocessing.Event()

			p = multiprocessing.Process(target=self.doJSON, name="doJSON", args=(driver, length, a, i,))
			q = multiprocessing.Process(target=self.foo, name="foo", args=(5,))

			p.start()
			q.start()

			self.foundIt.wait()
			
			self.quit.set()

			if p.is_alive():
				p.terminate()
			if q.is_alive():
				q.terminate()

			i = i + 1
			driver.close()

			# Put focus on current window which will be the window opener
			driver.switch_to_window(main_window)

			self.foundIt = None
			self.quit = None

		
if __name__ == "__main__":

	file = open('pdxstartups.json', 'w+')

	with file as outfile:
		fullFunc(outfile)
		file.close()



# Class not used yet
class PDXStartupsAPI:
	def __init__(self, ID, title, company, location, date, languages, link):
		def __repr__(self):
			return "ID: %s, title: %s, comapny: %s, location: %s, date: %s, languages: %s, link: %s" % (self.id, self.title, self.company, self.location, self.date, self.languages, self.link)
		def __str__(self):
			return "ID: %s, title: %s, comapny: %s, location: %s, date: %s, languages: %s, link: %s" % (self.id, self.title, self.company, self.location, self.date, self.languages, self.link)

		self.id = ID # check
		self.title = title # check
		self.company = None
		self.location = location # check
		self.date = date # check
		self.languages = [] # check
		self.link = link # check
		self.salary = None
		self.hours = None
		self.experience = None

