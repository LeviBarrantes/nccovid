from django.http import JsonResponse
from django.shortcuts import render
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


def welcome(request):
    browser = webdriver.Chrome(executable_path="/chromedriver.exe")

    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})


def overview(request):
    browser = webdriver.Chrome(executable_path="/chromedriver.exe")

    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})


def save_covid_info(request):

    result = requests.get(url='',
                          params={})

    soup = BeautifulSoup(result.content)

    new_info.save()
    return JsonResponse({"Success": "true"})


def show(request):
    browser = webdriver.Chrome(executable_path="/chromedriver.exe")

    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})


def get_stat_from_zip(request):

    zip = request.GET['zip_value']

    result = requests.get(url='http://api.openweathermap.org/data/2.5/weather',
                          params={"zip": zip,
                                  "appid": "",
                                  "units": "metric"})

    result_dictionary = result.json()
    city = result_dictionary['name']

    return JsonResponse({"Zip": zip,
                         "City": city})


def findings(request):

    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})


def conclusion(request):

    return render(request=request,
                  template_name='main/show.html',
                  context={"all_info": all_info})