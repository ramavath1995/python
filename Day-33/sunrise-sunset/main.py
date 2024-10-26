import time
import smtplib
import requests
import datetime

LAT = 14.696869
LAN = 76.854652
FROM = "dhakya1995@gmail.com"
PASSWORD = "pytt lkgf uyrc byot"
TO = "dhakya31@gmail.com"

# http://api.open-notify.org/iss-now.json  api for get current iss_position

parameters = {
    "lat": LAT,
    "lng": LAN,
    "formatted": 0
}


def over_headed():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if LAT - 5 <= iss_latitude <= LAT + 5 and LAN - 5 <= iss_longitude <= LAN + 5:
        return True


def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = sunrise.split("T")[1].split(":")[0]
    sunset_hour = sunset.split("T")[1].split(":")[0]
    hour = datetime.datetime.now().hour
    if sunrise_hour < hour or sunset_hour > hour:
        return True


while True:
    time.sleep(60)
    if over_headed() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(f"{FROM}:587", PASSWORD)
        connection.sendmail(from_addr=FROM, to_addrs=TO, msg="Subject:Look Up\n\niss_position above the sky")
