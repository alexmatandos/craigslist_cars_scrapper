import pandas
import os
from bs4 import BeautifulSoup
import glob
from datetime import datetime

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

for file in glob.glob("car_html_files/*.html"):
	result_list = {}
	f = open(file, encoding = "UTF-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	
	prices = soup.find("span", {"class": "price"})
	if prices == None:
		price = ""
	else:
		price = prices.text.replace("$", "").replace(",", "")
	result_list['price'] = price		
	
	attrgroups = soup.find_all("p", {"class" : "attrgroup"})
	model = attrgroups[0].text.replace('\n', '').replace('\r','')
	car_age = datetime.now().year - int(model[0:5])
	
	result_list['model'] = model
	result_list['price'] = price
	result_list['car age'] = car_age
	
	span = attrgroups[1].find_all("span")
	for x in span:
		value = x.find("b")
		if value != None:
			value = value.text
			attribute = x.text.replace(value, "").strip()
		else:
			value = ""
		result_list[attribute] = value

	if result_list:
		df = df.append(result_list, ignore_index = True)
		df = df.drop_duplicates()
df.to_csv("parsed_files/craigslist_cars.csv")


		

		

	
	
	



	
