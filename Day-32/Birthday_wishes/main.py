import random
import smtplib
import datetime as dt
import pandas

FROM = "dhakya1995@gmail.com"
PASSWORD = "pytt lkgf uyrc byot"
TO = "dhakya31@gmail.com"


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birth_day = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birth_day:
    birth_day_person = birth_day[today_tuple]
    file = f"letters/letter_{random.randint(1,3)}.txt"
    with open(file) as greetings:
        name = greetings.read()
        z = name.replace("[Name]", birth_day_person["name"])

    with smtplib.SMTP("smtp.gmail.com:587") as connection:
        connection.starttls()
        connection.login(user=FROM, password=PASSWORD)
        connection.sendmail(from_addr=FROM,
                            to_addrs=birth_day_person["email"],
                            msg=f"Subject:Success\n\n{z}")
