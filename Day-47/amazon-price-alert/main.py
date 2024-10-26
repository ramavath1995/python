from bs4 import BeautifulSoup
import requests
import smtplib

amazon_url = "https://www.amazon.in/iQOO-Snapdragon-Processor-Supercomputing-Flagship/dp/B07WJVY42H/ref=sr_1_1_sspa?crid=ZT2AZN06B38O&dib=eyJ2IjoiMSJ9.tj0o7NuZo20zFNzHtEVbN6YdfHOQoiLHqG6zVzkVX7tbi92IcafltYnZ3nMX76UMD3YO1gEutMvy5rGi0Z-McZ7fvG76dUFKr2VC5eIiuyk_s7so7wBEDxOz-qfL6Ur8sCVm-JJLBR44OS6VEwTJQ6jSgI921XyO9FwpR7Gmp7lhB-vnkePUnbJtTPPFDsFXpvGjAfj6Wph1sjMm96T73rXYQWwAOlxbaDO6mixlAD5oakF4jaq-4ZY5djMog4nwfFg0sHWXF8AZ-rFZBUxtqZuR4A-Mh_6FgNh1GB_4p9U.F4ldAoKZs_D22Im52nlrhV1zHi8GhpqF4P9xNpc1ZUA&dib_tag=se&keywords=iqoo%2Bneo%2B9%2Bpro&qid=1710929688&s=electronics&sprefix=iqoo%2B%2Celectronics%2C300&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=amazon_url, headers=head)
contents = response.text

soup = BeautifulSoup(contents, "lxml")
price = soup.find(name="span", class_="a-price-whole")
item_price = price.getText().strip().split(".")[0]
f_price = item_price.split(",")[0]
s_price = item_price.split(",")[1]
whole_price = int(f_price+s_price)
FROM = "dhakya1995@gmail.com"
PASSWORD = "pytt lkgf uyrc byot"
TO = "dhakya31@gmail.com"
if whole_price <= 35000:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(FROM, PASSWORD)
    connection.sendmail(from_addr=FROM, to_addrs=TO, msg=f"Subject:Price alert\n\nYour product price reduced to {int(item_price)}. Buy now")
    connection.close()
