import smtplib
import datetime as dt
import random

with open('quotes.txt', mode='r') as file:
    data = file.readlines()

time = dt.datetime.now()

gmail_addr = "peakyblinder130307@gmail.com"
gmail_pass = "%%3sG%53wk$w5Pyex"

yahoo_addr = "amilasuvan@yahoo.com"
yahoo_pass = "jmEEG6+5s%EI1h"

key = 'zwngjcteoctwxwne'

if time.weekday() == 0:
    msg_quote = random.choice(data)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=gmail_addr, password=key)
        connection.sendmail(from_addr=gmail_addr, to_addrs=yahoo_addr, msg=f'Subject: Monday Motivation\n\n{msg_quote}')

# with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=yahoo_addr, password=yahoo_pass)
#     connection.sendmail(from_addr=yahoo_addr, to_addrs=gmail_pass, msg='Subject: Hell gmail\n\nThis practice 2')