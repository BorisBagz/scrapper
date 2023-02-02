import urllib.request
with urllib.request.urlopen('https://www.pricesmart.com/site/pa/es/pagina-producto/956696') as response:
   html = response.read()
   html_decoded = html.decode("utf-8")
   print(html_decoded)
