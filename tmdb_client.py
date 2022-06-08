import requests


def get_popular_movies():
    end_point = "https://api.themoviedb.org/3/movie/popular"
    api_token = "87103682f4ed4527cd3b63d35572fe72"
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