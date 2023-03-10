#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import date
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the certificate warning from url request
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

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
price = soup.find(id="product-price").text

#formatting the output
formattedString = "\nExisten <b>{}</b> unidades de <b>{}</b> en la sucursal de <b>{}</b>.\n\nAhora cuestan <b>{}</b>. \n\n Puedes revisar el enlace acá: {} ".format(quantityOnStock,productName,clubName,price,URL)

#remove tabulations and newlines
emailContent = re.sub('\s+',' ', formattedString)

#opening and writing into txt file
file = open("EMAIL.txt", "w")
file.write(emailContent)
file.close()

#getting todays date and time for format
today = date.today()
currentDateAndTime = datetime.now()
myTime = currentDateAndTime.strftime("%H:%M")

#concatenating the final command to execute
commandToExecute = "mailx -s \"Tracking - Pads Wolfy en PriceSmart - {} - {}\" bagzscrapper-main@altmails.com < EMAIL.txt".format(today, myTime)

#launching the command and sending the email
os.system(commandToExecute)
