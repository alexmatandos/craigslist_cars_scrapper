import pandas
import os
from bs4 import BeautifulSoup
import glob
import re
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
	
	attrgroups = soup.find_all("p", {"class" : "attrgroup"})
	info = attrgroups[0].text.replace('\n', '').replace('\r','').upper()
	res = [int(i) for i in info.split() if i.isdigit()]
	model_year = res[0]
	model = info.replace(str(model_year), "").replace(" ", "", 1)
	car_age = datetime.now().year + 1 - model_year
	
	if model == "":
		model = "N/A"

	if model[0] == " ":
		model = model. replace(" ", "", 1)
	brand = model.split()[0]

	japanese = 0
	manufacturers = ['TOYOTA','HONDA', 'NISSAN', 'MAZDA', 'SUBARU', 'ISUZU', 'SUZUKI', 'MITSUBISHI', 'LEXUS', 'ACURA', 'INFINITI']
	for manufacturer in manufacturers:
		if brand == manufacturer:
			japanese = 1

	result_list['MODEL'] = model
	result_list['PRICE'] = price
	result_list['MODEL YEAR'] = model_year
	result_list['CAR AGE'] = car_age
	result_list['JAPANESE'] = japanese

	span = attrgroups[1].find_all("span")
	for x in span:
		value = x.find("b")
		if value != None:
			value = value.text
			attribute = x.text.replace(value, "").replace(":", "").strip().upper()
		else:
			value = ""
		result_list[attribute] = value

	if result_list:
		df = df.append(result_list, ignore_index = True)
		df = df.drop_duplicates()
df.to_csv("parsed_files/craigslist_cars.csv")


		

		

	
	
	



	
