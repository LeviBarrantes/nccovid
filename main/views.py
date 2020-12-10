from django.http import JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# This function activates when trying to go to the home page, or on first entry.
# Calls for index to be shown.
from main.models import *


def index(request):
    return render(request, template_name="main/index.html")


# This function goes when someone wants to see some local news tidbits, and calls the corresponding html page.
def news(request):
    return render(request, template_name="main/news.html")


# This function goes when someone wants to donate, and calls the corresponding html page.
def donate(request):
    return render(request, template_name="main/donate.html")


def searchbyzipcode(request):
    return render(request, template_name='main/searchbyzipcode.html')


def legal(request):
    return render(request, template_name='main/legal.html')


# This takes the zip from the user calls to a weather API to get the city, and temperature of that town if wanted.
# Everything comes in as a dictionary. Returns it the same way formatted as Json.
def get_zip(request):
    zip = request.GET['zip_value']

    result = requests.get(url='http://api.openweathermap.org/data/2.5/weather',
                          params={"zip": zip,
                                  "appid": "f61c33e090b420a8b963b3b31ccd8a9b",
                                  "units": "metric"})

    result_dictionary = result.json()
    city = result_dictionary['name']

    return JsonResponse({"zip": zip,
                         "city": city})


def get_news_data(request):
    """Function to get the first five covid related articles from major news sources as well as local news sources.
       Currently, there are two major publications (NY Times and USA Today) and three local news sources"""

    # search_term_1 = request.GET['search_term_1'] - right now the parameter 'covid' is hard coded, can leave as is
    # The following requests are accessing each news site and "searching" for covid related articles
    nytimes_data = requests.get(url='https://www.nytimes.com/search',
                                params={'query': 'covid'})

    usa_today_data = requests.get(url='https://www.usatoday.com/search/',
                                  params={'q': 'covid'})

    wral_data = requests.get(url='https://www.wral.com/charlotte/17382438/')

    wcnc_charlotte_data = requests.get(url='https://www.wcnc.com/search',
                                       params={'q': 'covid'})

    wccb_clt_data = requests.get(url='https://www.wccbcharlotte.com/search/covid')

    # Using BeautifulSoup on the data that that has been scrapped
    soup_nytimes_data = BeautifulSoup(nytimes_data.content)
    soup_usa_today_data = BeautifulSoup(usa_today_data.content)
    soup_wral_data = BeautifulSoup(wral_data.content)
    soup_wcnc_charlotte_data = BeautifulSoup(wcnc_charlotte_data.content)
    soup_wccb_clt_data = BeautifulSoup(wccb_clt_data.content)

    # Retrieving the article titles
    nytimes_titles = soup_nytimes_data.find_all(name="h4",
                                                attrs={"class": "css-2fgx4k"})

    usa_today_titles = soup_usa_today_data.find_all(name="a",
                                                    attrs={"class": "gnt_se_a gnt_se_a__hd gnt_se_a__hi"})

    wral_titles = soup_wral_data.find_all(name="strong")

    wcnc_charlotte_titles = soup_wcnc_charlotte_data.find_all(name="a",
                                                              attrs={"class": "search__title-link"})

    wccb_clt_titles = soup_wccb_clt_data.find_all(name="h3",
                                                  attrs={"class": "h3 entry-title"})

    # The following for-loops are used to limit the number of articles being scrapped from each site to 5
    count = 0
    for title in nytimes_titles:
        new_title = NYTimes(article_title=title.text)
        new_title.save()
        count += 1
        if count == 5:
            break

    count = 0
    for title in usa_today_titles:
        new_title = USAToday(article_title=title.text)
        new_title.save()
        count += 1
        if count == 5:
            break

    count = 0
    for title in wral_titles:
        new_title = WRAL(article_title=title.text)
        new_title.save()
        count += 1
        if count == 5:
            break

    count = 0
    for title in wcnc_charlotte_titles:
        new_title = WCNC(article_title=title.text)
        new_title.save()
        count += 1
        if count == 5:
            break

    count = 0
    for title in wccb_clt_titles:
        new_title = WCCB(article_title=title.text)
        new_title.save()
        count += 1
        if count == 5:
            break

    # Print statements used to check if the data was being scraped via IDE console, can delete after integration
    count = 0
    print("-----Articles from 'New York Times'-----")
    for title in nytimes_titles:
        print(title.text)
        count += 1
        if count == 5:
            break

    count = 0
    print("\n-----Articles from 'USA TODAY'-----")
    for title in usa_today_titles:
        print(title.text)
        count += 1
        if count == 5:
            break

    count = 0
    print("\n-----Articles from 'WRAL Charlotte'-----")
    for title in wral_titles:
        print(title.text)
        count += 1
        if count == 5:
            break

    count = 0
    print("\n-----Articles from 'WCNC Charlotte'-----")
    for title in wcnc_charlotte_titles:
        print(title.text)
        count += 1
        if count == 5:
            break

    count = 0
    print("\n-----Articles from 'WCCB Charlotte'-----")
    for title in wccb_clt_titles:
        print(title.text)
        count += 1
        if count == 5:
            break

    usa_today_all = USAToday.objects.all()
    ny_times_all = NYTimes.objects.all()
    wccb_all = WCCB.objects.all()
    wcnc_all = WCNC.objects.all()
    wral_all = WRAL.objects.all()

    # Return statement not working, need to fix link to 'display template'
    return render(request,
                  template_name='main/news.html',
                  context={"ny_times_all": ny_times_all,
                           "usa_today_all": usa_today_all,
                           "wccb_all": wccb_all,
                           "wcnc_all": wcnc_all,
                           "wral_all": wral_all})
