import tmdb_client
from unittest.mock import Mock

#Testing single movie
def test_get_single_movie(monkeypatch):
   mock_movie_list = ['Movie 1']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movie_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_list = tmdb_client.get_single_movie(movie_id=550)
   assert movie_list == mock_movie_list

#Testing endpoint for single movie
def test_endpoint_single_movie():
   selected_id = 550
   url = tmdb_client.endpoint_single_movie(movie_id=selected_id)
   assert url == f"https://api.themoviedb.org/3/movie/{selected_id}"
   
#Testing movie images
def test_get_movie_images(monkeypatch):
   mock_image_list = ['Image 1']
   id = 550
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_image_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   image_list = tmdb_client.get_movie_images(movie_id=id)
   assert image_list == mock_image_list

#Testing endpoint for get_movie_images
def test_endpoint_get_movie_images():
   selected_id = 550
   url = tmdb_client.endpoint_get_movie_images(movie_id=selected_id)
   assert url == f"https://api.themoviedb.org/3/movie/{selected_id}/images"

#Testing single_movie_cast
def test_get_single_movie_cast(monkeypatch):
   mock_cast_list = ['Cast 1']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_cast_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   image_list = tmdb_client.get_single_movie_cast(movie_id=550)
   assert image_list == mock_cast_list

#Testing endpoint for get_single_movie_cast
def testendpoint_get_single_movie_cast():
   selected_id = 550
   url = tmdb_client.endpoint_get_single_movie_cast(movie_id=selected_id)
   assert url == f"https://api.themoviedb.org/3/movie/{selected_id}/credits"