import os
from bs4 import BeautifulSoup
import glob
import re

for file in glob.glob("car_html_files/*.html"):
	f = open(file, encoding = "UTF-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	prices = soup.find("span", {"class": "price"})
	if prices == None:
		price = "N/A"
	else:
		price = prices.text.replace("$", "").replace(",", "")
	
	infos = soup.find_all("p", {"class": "attrgroup"})
	vehicle = infos[0].text
	year = vehicle[0:5]
	name = vehicle[6: len(vehicle)]
	more_info = infos[1]
	spans = more_info.find_all("span")
	
	for span in spans:
		values = span.find("b")
		if values == None:
			value = "N/A"
			category = "N/A"
		else:
			value = values.text
			category = span.text.replace(value, "")
		

		

	
	
	



	
