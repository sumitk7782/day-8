#------------------Email send to automation----------------

import smtplib
import ssl

sender_email = "YOUR EMAIL"
password = "qyit oxbi babhy oscq"   
receiver_email = "RECEVIER_EMAIL"
message = "Hello! This is a test email."

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
