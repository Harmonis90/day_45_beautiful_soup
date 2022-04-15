from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
# ----------------------------------------------- Intro To BS4 ----------------------------------------------- #
# with open("./website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# urls = soup.find_all("a")
# for tag in urls:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# other_headings = soup.find_all(class_="heading")
# for heading in other_headings:
#     print(heading.string)
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
# ----------------------------------------------- Live Site Scraping ----------------------------------------------- #
# My Way... Messy lol
# response = requests.get("https://news.ycombinator.com/")
# response.raise_for_status()
# data = response.text
#
# soup = BeautifulSoup(data, "html.parser")
# title_links = soup.find_all(class_="titlelink")
# scores = soup.find_all(class_="score")
# for score in scores:
#     print(score.text)
# for link in title_links:
#     print(f"{link.text}:{link.get('href')}")
# More precise way
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


article_tags = soup.find_all(name="a", class_="titlelink")
article_texts = [text.get_text() for text in article_tags]
article_links = [links.get("href") for links in article_tags]
article_scores = [int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

max_score = article_scores.index(max(article_scores))
print(f"{article_scores[max_score]} Upvotes:\n\t{article_texts[max_score]}\n\t{article_links[max_score]}")
