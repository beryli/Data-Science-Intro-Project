import pandas as pd
import numpy as np
import urllib.request
import bs4
import re
import csv

def getData(url, feature_list):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	req = urllib.request.Request(url=url, headers=headers)
	data = urllib.request.urlopen(req).read()
	root = bs4.BeautifulSoup(data, "html.parser")

	items = root.findAll(class_= 'prdct-item clearfix card')
	for item in items:
		features = []
		detail = item.find(class_= 'prdct-item__prc-val',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__name',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue

		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--cpu')
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--ram',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--strge',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--bttry',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue

		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--cmra',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--aspct',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--sim',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		detail = item.find(class_= 'prdct-item__spcftn kyspc__item--os',text=True)
		if detail is not None:
			features.append(detail.text)
		else:
			continue
		feature_list.append(features)
# getting raw data from the website of each page

url = ""
feature_list = []

for i in range(1, 61):
	if i == 1:
		url = "https://www.mysmartprice.com/mobile/pricelist/mobile-price-list-in-india.html"
	else:
		url = "https://www.mysmartprice.com/mobile/pricelist/pages/mobile-price-list-in-india-" + str(i) + ".html"
	getData(url, feature_list)
	print(i)

df = pd.DataFrame(feature_list)
df.to_excel("rawData.xlsx")

