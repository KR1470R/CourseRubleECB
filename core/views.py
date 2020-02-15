from django.shortcuts import render
from django.views.generic import ListView
import urllib.request
import xmltodict
from bs4 import BeautifulSoup
import json

def mainPage(request):
## parsiing
	#get from ECB##
	def get_html():
		global rate 
		global currency
		global soup
		currency = []
		rate = []
		file = urllib.request.urlopen("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml").read()
		soup = BeautifulSoup(file,'lxml')	
		for i in soup.findAll('cube', {'rate':True, 'currency':True}):
			rate.append(i['rate'])
		for j in soup.findAll('cube', {'currency':True}):
			currency.append(j['currency'])
	## get json date #		
	def get_json():
		global name 
		global value
		global data
		name = []
		value = []
		url = 'https://www.cbr-xml-daily.ru/daily_json.js'
		response = urllib.request.urlopen(url)
		data = json.loads(response.read())
		for i in data['Valute']:
			value.append(data['Valute'][i]['Value'])
		for j in data['Valute']:
			name.append(j)
	try:
		get_html()
		return render(request,'index.html',
			{'rate':rate, 'currency':currency})
	except:
		get_json()
		return render(request,'index.html', 
			{'rate':value, 'currency':name})

def aboutPage(request):
	return render(request, 'about.html')