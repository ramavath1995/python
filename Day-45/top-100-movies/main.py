import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
result = soup.find_all(name="h3", class_="title")
all_movies = [movie.getText() for movie in result]
movies = all_movies[::-1]
with open("top_100_movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
