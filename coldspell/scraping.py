#
# Name: Ben Liu
# Filename: scraping.py
# Description: Python file performing the scraping as well as the displaying of scraped data
# Citations: Web Scraping Tutorial - https://stepupanalytics.com/web-scraping-tutorial-using-python-part-1/
#

from bs4 import BeautifulSoup
from numpy import mean
import requests
import re

URL = "https://forecast.weather.gov/MapClick.php?lat=40.98&lon=-74.99&lg=english&FcstType=text#.XkKwJxNKhQJ"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast-body")
forecast_items = seven_day.find_all(class_="forecast-tombstone")
temps = []

for day in forecast_items:
    print(day.find(class_="period-name").get_text())
    print(day.find(class_="short-desc").get_text())
    try:
        high = day.find(class_="temp temp-high").get_text()
        print(high + "\n")
        highnum = int(re.sub("[^0-9]", "", high))
        temps.append(highnum)
    except:
        low = day.find(class_="temp temp-low").get_text()
        print(low + "\n")
        lownum = int(re.sub("[^0-9]", "", low))
        temps.append(lownum)

avgTemp = int(round(mean(temps), 0))
print("Average temp: " + str(avgTemp) + " °F")
if avgTemp <= 24:
    print("It will be really cold in the next couple days!")
elif avgTemp >= 25 and avgTemp <= 36:
    print("It will be cold in the next couple days!")
elif avgTemp >= 37 and avgTemp <= 52:
    print("It will be chilly in the next couple days!")
elif avgTemp >= 53 and avgTemp <= 60:
    print("It will be slightly chilly in the next couple days!")
elif avgTemp >= 61 and avgTemp <= 72:
    print("It will be comfortable in the next couple days!")