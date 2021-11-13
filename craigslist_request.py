import urllib.request
import os
from bs4 import BeautifulSoup
import time
import glob

if not os.path.exists("html_files"):
	os.mkdir("html_files")

if not os.path.exists("car_html_files"):
	os.mkdir("car_html_files")

for i in range(5):
	index = i*120
	f = open("html_files/page" + str(index) + ".html", "wb")
	response = urllib.request.urlopen("https://greenville.craigslist.org/d/cars-trucks-by-owner/search/cto?s=" + str(index))
	html = response.read()
	f.write(html)
	f.close()
	print(index)
	time.sleep(30)

for file in glob.glob("html_files/*.html"):
	f = open(file, encoding = "UTF-8")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	results = soup.find("ul", {"id": "search-results"})
	cars = results.find_all("li")

	for car in cars:
		tag = car.find("a")
		url = tag.get("href")
		link = url.replace("https://", "").replace("/", "")
		
		f = open("car_html_files/" + str(link), "wb")
		response = urllib.request.urlopen(url)
		html = response.read()
		f.write(html)
		f.close()
		print(link)
		time.sleep(30)