#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


URL = "https://www.pricesmart.com/site/pa/es/pagina-producto/956696"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="clubQuantity")

quantity = results.find("span", class_="d-none")

print(quantity)
