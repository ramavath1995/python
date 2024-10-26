import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+919493638582")
print(phone_number1)

print(geocoder.description_for_number(phone_number1, "en"))
