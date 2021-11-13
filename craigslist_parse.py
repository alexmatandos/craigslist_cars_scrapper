import os
from bs4 import BeautifulSoup
import time
import glob

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
	span = more_info.find_all("span")
	print(span)
	


	
