import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText().replace("â\x80\x93", "") for movie in all_movies]
movies = movie_titles[::-1]

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
