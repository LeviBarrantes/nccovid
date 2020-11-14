from django.http import JsonResponse
from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


# This function goes when someone wants to see some local news tidbits, and calls the corresponding html page.
def news(request):
    return render(request=request,
                  template_name='main/news.html',
                  context={})


# This function goes when someone wants to donate, and calls the corresponding html page.
def donate(request):
    return render(request=request,
                  template_name='main/donate.html',
                  context={})


# This function activates when trying to go to the cdc page.
# Calls for cdc to be shown.
def cdc(request):
    result = requests.get(url='',
                          params={})

    soup = BeautifulSoup(result.content)

    return render(request=request,
                  template_name='main/cdc.html',
                  context={})


# This function activates when trying to go to the home page, or on first entry.
# Calls for index to be shown.
def index(request):
    return render(request=request,
                  template_name='main/index.html')


# This takes the zip from the user calls to a weather API to get the city, and temperature of that town if wanted.
# Everything comes in as an easy to do dictionary. returns it the same way formatted as Json.
def get_zip(request):
    zip = request.GET['zip_value']

    result = requests.get(url='http://api.openweathermap.org/data/2.5/weather',
                          params={"zip": zip,
                                  "appid": "f61c33e090b420a8b963b3b31ccd8a9b",
                                  "units": "metric"})

    result_dictionary = result.json()
    city = result_dictionary['name']
    temp = result_dictionary['main']['temp']

    return JsonResponse({"zip": zip,
                         "city": city})
