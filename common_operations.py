import requests
from bs4 import BeautifulSoup


def get_movie_result(city):
    url = f"https://in.bookmyshow.com/explore/home/{city}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    movies_list = []
    all_movies = soup.find(
        "div", {"class": "style__RelativeContainer-sc-lnhrs7-0 jftWkf"}
    ).find_all("a")
    for data in all_movies:
        movie_info = data.find_all("div")
        movies_dict = {"movie_name": movie_info[-3].text, "genre": movie_info[-2].text}
        movies_list.append(movies_dict)
    return movies_list

def get_movie_info(city):
    url = f'https://in.bookmyshow.com/explore/movies-{city}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    movies = []
    for div in soup.find_all("div",{"class":"style__VerticalCardContainer-sc-dv5ht7-0 kKvMMQ"}):
        data = div.find_all("div")
        if len(data) > 5:
            name = data[5].text
            try:
                certificate = data[6].text if name!= data[6].text else data[7].text
            except:
                certificate =  data[5].text if not "" else data[4]
            try:
                launguage = data[8].text if certificate!= data[8].text else data[9].text
            except:
                launguage =  data[7].text if not "" else data[6]
            movies.append({
                "name":name,
                "certificate":certificate,
                "launguage":launguage,
            })
    return movies