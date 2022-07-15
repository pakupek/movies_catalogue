import requests
import random
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzEwMzY4MmY0ZWQ0NTI3Y2QzYjYzZDM1NTcyZmU3MiIsInN1YiI6IjYyOWY4ODY3ZDIxNDdjMTE3ZTYzZTNlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rmqYp6McgetjqfoH6uXJzJqlyBwVTZVyG8qTlY0glw8"
API_TOKEN2 = "87103682f4ed4527cd3b63d35572fe72"


list = ["popular","upcoming","top_rated","now_playing"]

#Downloading movie list
def get_movies_list(list_type):
    end_point = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(end_point, headers=headers)
    response.raise_for_status()
    return response.json()


#URL do pobierania plakatu
def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many] 

def endpoint_single_movie(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    id = str(movie_id)
    endpoint = base_url + id
    return endpoint

#API do pobrania filmu
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


#API do pobrania obsady filmu
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def endpoint_get_single_movie_cast(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    id = str(movie_id)
    cr = "/credits"
    endpoint = base_url + id + cr
    return endpoint

#API do pobrania zdjęć
def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images" 
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json() 

def endpoint_get_movie_images(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    img = "/images"
    id = str(movie_id)
    endpoint = base_url + id + img
    return endpoint

#API do wyszukiwania filmów
def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']


#API do pobrania listy filmów obecnie wyświetlanych
def get_airing_today():
    endpoint = "https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']

