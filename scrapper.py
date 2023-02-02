#!/usr/bin/python

import requests

URL = "https://www.pricesmart.com/site/pa/es/pagina-producto/956696"
page = requests.get(URL)

print(page.text)
