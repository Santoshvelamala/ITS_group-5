from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import requests
import json
import urllib
from django.http import HttpResponseRedirect
from .forms import NameForm

# Retreiving Kissans data from Server(Website-1) to Client(Website-2)

url = 'http://10.0.3.23:1996/kissans'
response = urllib.urlopen(url)
kissans =json.loads(response.read())


# Retreiving Farms data from Server(Website-1) to Client(Website-2)

url1 = 'http://10.0.3.23:1996/farms'
response1 = urllib.urlopen(url1)
dat2 = json.loads(response1.read())


# Retreiving Wells data from Server(Website-1) to Client(Website-2)

url2 = 'http://10.0.3.23:1996/wells'
response2 = urllib.urlopen(url2)
data = json.loads(response2.read())


# Retreiving Houses data from Server(Website-1) to Client(Website-2)

url3 = 'http://10.0.3.23:1996/houses'
response3 = urllib.urlopen(url3)
dat1 = json.loads(response3.read())


# Retreiving Family members data from Server(Website-1) to Client(Website-2)

url4 = 'http://10.0.3.23:1996/familymembers'
response4 = urllib.urlopen(url4)
dat3 = json.loads(response4.read())


# For Analytics (for pie chart)
def rend(request):
    return render(request,'clientapp/apple.html',context={'data':data,'dat1':dat1, 'dat2':dat2 } )



# Authentication for the Farmer(User) to login
# Only the data concerned with the particular user(i.e., houses, farms) will be retrieved and displayed in the maps

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
		P=form.cleaned_data['Phone']
		Pw=form.cleaned_data['Pwd']
		form = NameForm()
		for k in kissans:
			if str(k['Phone'])==P and k['Password']==Pw:
				request.session['K_id'] = k['id']
				data2=[]
				data1=[]
				data3=[]
    				for d in dat2:
					if d['F_id']==request.session['K_id']:
						data2.append(d)
				for d in dat1:
					if d['F_id']==request.session['K_id']:
						data1.append(d)
				for d in dat3:
					if d['F_id']==request.session['K_id']:
						data3.append(d)
		                return render(request,'clientapp/maps.html',context={'data':data,'data1':data1, 'data2':data2,'k':k,'data3':data3 } )	
    else:
        form = NameForm()

    return render(request, 'clientapp/name.html', {'form': form})



