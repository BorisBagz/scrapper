# importing yagmail and its packages
import yagmail

senderEmail = "bagzscrapper@gmail.com"
senderPwd = "borisscrapper"
receiverEmail = "borisbagz@gmail.com"

# initiating connection with SMTP server
yag = yagmail.SMTP(senderEmail,senderPwd)
# Adding Content and sending it
yag.send(receiverEmail,"TEST","this is a test")
