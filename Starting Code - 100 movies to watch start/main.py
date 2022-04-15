import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
movie_data = soup.find_all(name="h3", class_="title")

top_movie_list = [movie.get_text() for movie in movie_data]
movie_list = top_movie_list[::-1]


with open("Top_100_Movie_List.txt", "a") as file:
    for movie in movie_list:
        file.write(movie + "\n")
