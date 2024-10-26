from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/iQOO-Snapdragon-Processor-Supercomputing-Flagship/dp/B07WJVY42H/ref=sr_1_1_sspa?crid=2LPF7Z1OUN1XI&dib=eyJ2IjoiMSJ9.tj0o7NuZo20zFNzHtEVbN6YdfHOQoiLHqG6zVzkVX7u8K_9KmAWPeMmVopg1cXhLNVsbSeI_ovOiuTIcK00woSQQ5_C-ZbLMP-lisnjlTP6NovrjLaRtpxwFD5WKKi2PrX5Pnu6EnUSl_-nsm5nSVImbkQesGDWRLcc9RvxLA6ebCUUoEAB1xpTzspd8bGITQb6T5dNfuOW7p0Ol19rUeZb57nncZuX0xG5cySp1EXRoakF4jaq-4ZY5djMog4nwvS2Ybh6AUfxTkmZPltwDiZuR4A-Mh_6FgNh1GB_4p9U.cVoEecnZ-kQdJaqvbXVrjdhFKlcBFsPKbHdQmTdSReA&dib_tag=se&keywords=iqoo%2Bneo%2B9%2Bpro&qid=1710988753&s=electronics&sprefix=%2Celectronics%2C242&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
print(price.text)

driver.close()
