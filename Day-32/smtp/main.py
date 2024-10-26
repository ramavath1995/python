import smtplib

# Simple Mail Transfer Protocol (SMTP) is an application used by mail servers to send, receive,
# and relay outgoing email between senders and receivers
FROM = "dhakya1995@gmail.com"
PASSWORD = "pytt lkgf uyrc byot"
TO = "dhakya31@gmail.com"


with smtplib.SMTP("smtp.gmail.com:587") as connection:
    connection.starttls()
    connection.login(user=FROM, password=PASSWORD)
    connection.sendmail(from_addr=FROM,
                        to_addrs=TO,
                        msg="Subject:Success\n\nI did it")
