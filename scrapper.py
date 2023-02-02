from urllib.request import urlopen

url = "https://www.pricesmart.com/site/pa/es/pagina-producto/956696"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)
