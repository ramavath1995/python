from bs4 import BeautifulSoup

with open("my_data.html") as file:
    contents = file.read()

s = BeautifulSoup(contents, "html.parser")
print(s.title)