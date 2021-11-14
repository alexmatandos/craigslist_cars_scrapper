import pandas
import os
from bs4 import BeautifulSoup
import glob
import re

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

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
	year = vehicle[0:5].replace("\n", "").replace("\r", "")
	name = vehicle[6: len(vehicle)]
	name_split = name.split()
	manufacturer = name_split[0]
	model = name.replace(manufacturer, "")
	more_info = infos[1]
	spans = more_info.find_all("span")
	
	for span in spans:
		values = span.find("b")
		if values == None:
			value = "N/A"
			category = "N/A"
		else:
			value = values.text
			category = span.text.replace(value, "").replace(":","")
			category = category.split()
		
		if category == ['fuel']:
			fuel = value
			
		if category == ['odometer']:
			mileage = value
			
		if category == ['transmission']:
			transmission = value
			
		if category == ['title', 'status']:
			title = value
			
		if category == ['condition']:
			condition = value
			
		if category == ['cylinders']:
			engine = value

	df = df.append({
		'Year': year,
		'Manufacturer': manufacturer,
		'Model': model,
		'Price': price,
		'Fuel': fuel,
		'Mileage': mileage,
		'Transmission': transmission,
		'Title': title
		}, ignore_index = True)
	df = df.drop_duplicates()

df.to_csv("parsed_files/craigslist_cars.csv")	


		

		

	
	
	



	
