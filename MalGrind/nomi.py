import sys, os
import abc
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def searchDrug(url):
	return

driver = webdriver.Chrome("C:/Users/Faizan/Desktop/MalGrind/chromedriver")

def searchWebsite(id):
	driver.get("http://www.druginfosys.com/categorybrands.aspx?cat="+id)
	response = driver.page_source
	soup = BeautifulSoup(response, "html.parser")
	drugList = soup.find("table", { "id" : "ContentPlaceHolder1_DGrid" })

	f = open(id+'.html','w')
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

searchWebsite("25.2.2");


	
