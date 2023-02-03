#!/usr/bin/python

import requests
from bs4 import BeautifulSoup


URL = "https://www.pricesmart.com/site/pa/es/pagina-producto/956696"
page = requests.get(URL, verify=False)

soup = BeautifulSoup(page.content, "html.parser")

productName = soup.find(id="product-display-name").text
quantityOnStock = soup.find(id="clubQuantity").text
clubName = soup.find(id="club-name-description").text

print("\nExisten {} unidades de {} en la sucursal de {}".format(quantityOnStock,productName,clubName))
