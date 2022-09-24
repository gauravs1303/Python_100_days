import pandas
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

present = dt.datetime.now()
letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv').to_dict(orient='records')

for x in range(len(data)):
    # 2. Check if today matches a birthday in the birthdays.csv
    if data[x]['day'] == present.day and data[x]['month'] == present.month:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letter_choice = random.choice(letters)
        with open(file=letter_choice, mode='r') as file:
            letter_body = file.read()
        main_body = letter_body.replace('[NAME]', data[x]['name'])
        to_address = data[x]['email']
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user='peakyblinder130307@gmail.com', password='zwngjcteoctwxwne')
            connection.sendmail(to_addrs=to_address, from_addr='peakyblinder130307@gmail.com',
                                msg=f'Subject: Happy Birthday\n\n{main_body}')
