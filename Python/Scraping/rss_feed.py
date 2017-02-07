import feedparser
import json, os, sys, re
import requests
import urllib2
from bs4 import BeautifulSoup
from xml.etree import ElementTree as etree

arr = {}

class StackOverflowRSS:
	def __init__(self, ID, title, company, location, date, languages, link):
		def __repr__(self):
			return "ID: %s, title: %s, comapny: %s, location: %s, date: %s, languages: %s, link: %s" % (self.id, self.title, self.company, self.location, self.date, self.languages, self.link)
		def __str__(self):
			return "ID: %s, title: %s, comapny: %s, location: %s, date: %s, languages: %s, link: %s" % (self.id, self.title, self.company, self.location, self.date, self.languages, self.link)

		self.id = ID
		self.title = title
		self.company = company
		self.location = location
		self.date = date
		self.languages = []
		self.link = link
		self.salary = None
		self.hours = None
		self.experience = None# 

def retValues(ID, title, company, location, datePublished, languages, link):
	loop = "["
	length = len(languages)
	num = 0
	for l in languages:
		loop = loop + "\"" + l + "\""
		num = num + 1
		if (num < length):
			loop = loop + ", "
	loop = loop + "]"
	string = "{\"id\": " + ID + ", \"title\": \"" + title +  "\", \"company\": \"" + company + "\", \"location\": \"" + location + "\", \"date\": \"" + datePublished + "\", \"languages\": " + loop + ", \"link\": \"" + link + "\"}"
	return string

def convertFile(outfile):
	outfile.write("{\n")
	i = 0
	length = len(feeds.entries)
	for feed in feeds.entries:
		ID = ""
		title = ""
		company = ""
		location = ""
		datePublished = ""
		link = ""
		languages = []
		try:
			for t in feed.tags:
				languages.append(t.term)
		except:
			pass
		try:
			ID = feed.id
		except:
			pass
		try:
			title = feed.title
		except:
			pass
		try:
			company = feed.author
		except:
			pass
		try:
			location = feed.location
		except:
			pass
		try:
			datePublished = feed.published
		except:
			pass
		try:
			link = feed.link
		except:
			pass
		
		# For writing JSON file
		outfile.write("\"" + str(i) + "\":")
		x = retValues(ID, title, company, location, datePublished, languages, link)

		json.dump(x, outfile)
	 	i = i + 1
	 	if (i < length):
	 		outfile.write(",\n")
	outfile.write("}")




python_so_rss_url = urllib2.urlopen("http://stackoverflow.com/jobs/feed?tl=api")

feeds = feedparser.parse( python_so_rss_url )

file = open('data.json', 'w')

with file as outfile:
	convertFile(outfile)
	file.close()