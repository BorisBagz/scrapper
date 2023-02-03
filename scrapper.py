#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

#loading the desired product web page
URL = "https://www.pricesmart.com/site/pa/es/pagina-producto/956696"

#fetching the html code of the page
page = requests.get(URL, verify=False)

#parsing it for BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

#extracting the values of desired parameters
productName = soup.find(id="product-display-name").text
quantityOnStock = soup.find(id="clubQuantity").text
clubName = soup.find(id="club-name-description").text

#formatting the output
print("\nExisten {} unidades de {} en la sucursal de {}".format(quantityOnStock,productName,clubName))


client = vonage.Client(key="0d18ddf8", secret="vVKVcDa16abWlBWg")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "50763239627",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
#else:
#    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
