#!/usr/bin/python
import yagmail

receiver = "borisbagz@gmail.com"
body = "Hello there"

yag = yagmail.SMTP("borisbagz@gmail.com")
yag.send(
    to=receiver,
    subject="TEST TEST TEST",
    contents=body,
)
