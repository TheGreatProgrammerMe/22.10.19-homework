from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from django.conf import settings

def inflation_view(request):
	template_name = 'inflation.html'
	contextrez = []
	with open(settings.INFLATION_RUSSIA_CSV, newline='', encoding='utf-8') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';')
		contexkeys = ['Year', 'Yan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec', 'Total']
		for row in reader:
			mycontext = {
			'Year': None,
			'Yan': None,
			'Feb': None,
			'Mar': None,
			'Apr': None,
			'Mai': None,
			'Jun': None,
			'Jul': None,
			'Aug': None,
			'Sep': None,
			'Okt': None,
			'Nov': None,
			'Dec': None,
			'Total': None
			}
			sumisnone = 0 
			if row[0] != 'Год':
				for i in range(14):
					if (len(row[i])>0) and (not(i ==13 and sumisnone == 1)):
						mycontext[contexkeys[i]] = row[i]
					else:
						mycontext[contexkeys[i]] = '-'
						if sumisnone == 0:	
							mycontext[contexkeys[13]] = '-'
							sumisnone = 1
	
				contextrez.append(mycontext)
	return render(request, template_name, context  = {'contextrez': contextrez})
