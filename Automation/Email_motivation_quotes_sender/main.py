import random
import smtplib

my_email = " "
my_password = " "
email_to_forward = " "
import datetime as dt

day_name=["monday","tuesday"]
now = dt.datetime.now()
date = str(now.date())
day = dt.datetime.strptime(date, '%Y-%m-%d').weekday()

if day_name[day] == "tuesday":
    with open("quotes.txt") as data:
        quote = data.readlines()
        quotes = random.choice(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email_to_forward,
                            msg=f"subject:Motivation Quotes\n\n{quotes}")
