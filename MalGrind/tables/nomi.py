import sys, os
import abc
import re
import urlparse
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/Users/Faizan/Desktop/MalGrind/chromedriver")

def searchDrug(url):
	driver.get(url)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	drugList = soup.find_all("td", { "class" : "small" })
	for it in drugList:
		for x in it.find_all("a"):
			if re.search(r'aspx\?cat=[2-9][5-9]', str(x['href'])) is not None:
				searchWebsite(str(x['href']))

def searchWebsite(url):
	parsed = urlparse.urlparse("http://www.druginfosys.com/"+url)
	id = urlparse.parse_qs(parsed.query)['cat']
	driver.get("http://www.druginfosys.com/categorybrands.aspx?cat="+str(id[0]))
	response = driver.page_source
	soup = BeautifulSoup(response, "html.parser")
	drugList = soup.find("table", { "id" : "ContentPlaceHolder1_DGrid" })

	f = open(str(id[0])+'.html','w')
	f.write(str(drugList))

	try:
		for y in range(2,1000):
			if (y%5 != 1): 
				driver.find_element_by_xpath("""//*[@id="ContentPlaceHolder1_DGrid"]/tbody/tr[22]/td/a[contains(text(),'"""+str(y)+"')]").click()
			else:
				i = 5 if (y == 6) else 6
				driver.find_element_by_xpath("""//*[@id="ContentPlaceHolder1_DGrid"]/tbody/tr[22]/td/a["""+str(i)+"]").click()
			response = driver.page_source
			soup = BeautifulSoup(response, "html.parser")
			drugList = soup.find("table", { "id" : "ContentPlaceHolder1_DGrid" })
			f.write(str(drugList))
	except:
		pass

	f.close()

searchDrug("http://www.druginfosys.com/category.aspx")