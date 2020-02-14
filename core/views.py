from django.shortcuts import render
import urllib.request
import xmltodict
from bs4 import BeautifulSoup
def mainPage(request):
	currency = []
	rate = []
	## parsiing
	file = urllib.request.urlopen("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml").read()
	soup = BeautifulSoup(file,'lxml')	
	#for i in soup.findAll('cube'):
	#	print(i['rate'])
	for i in soup.findAll('cube', {'rate':True, 'currency':True}):
		print(i['rate'])
		rate.append(i['rate'])
	for j in soup.findAll('cube', {'currency':True}):
		print(j['currency'])
		currency.append(j['currency'])
	return render(request,'index.html', 
		{'rate':rate, 'currency':currency})

def aboutPage(request):
	return render(request, 'about.html')