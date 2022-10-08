import requests
import re
from bs4 import BeautifulSoup


def get_google():


    url = 'https://finance.yahoo.com/quote/GOOG/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    html_content = str(soup)

    matches = re.findall(r'GOOG\" data-test=\"qsp-price\" data-trend=\"none\" value=\"\d+.\d+\">\d+.\d+</fin-streamer>',  html_content)

    price_matches = re.findall(r'\d+.\d+',  matches[0])

    return price_matches[0]

