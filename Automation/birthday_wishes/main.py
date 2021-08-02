import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
day = now.day
month = now.month
MY_EMAIL = " "
MY_PASSWORD = " "
NAME = ""

df = pandas.read_csv("birthdays.csv")
bday_dict = df.to_dict(orient="records")

for bday in bday_dict:
    if bday["month"] == month and bday["day"] == day:
        NAME = bday["name"]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            mail = letter.read()
            mail = mail.replace("[NAME]", NAME)
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=f"{bday['email']}",
                                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{mail}".encode("utf-8"))
