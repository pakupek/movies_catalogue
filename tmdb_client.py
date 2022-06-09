import requests


def get_popular_movies():
    end_point = "https://api.themoviedb.org/3/movie/popular/"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzEwMzY4MmY0ZWQ0NTI3Y2QzYjYzZDM1NTcyZmU3MiIsInN1YiI6IjYyOWY4ODY3ZDIxNDdjMTE3ZTYzZTNlYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rmqYp6McgetjqfoH6uXJzJqlyBwVTZVyG8qTlY0glw8"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(end_point, headers=headers)
    return response.json()

get_popular_movies()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many] 