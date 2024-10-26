import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")

s = BeautifulSoup(response.text, "html.parser")
soup = s.find_all(name="span", class_="titleline")
article_titles = []
article_links = []
votes = []
for article in soup:
    article_titles.append(article.getText())
    article_links.append(article.contents[0].get("href"))
up_votes = [int(vote.getText().split()[0]) for vote in s.find_all(name="span", class_="score")]
print(up_votes)
highest_votes = max(up_votes)
article_index = up_votes.index(highest_votes)
top_article = article_titles[article_index]
top_article_link = article_links[article_index]
print(top_article)
print(top_article_link)
