from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for, flash
import tmdb_client
import random
from flask import abort
import datetime

app = Flask(__name__)
FAVORITES = set()
app.secret_key = b'my-secret'

#Pobieranie zdjęć
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


#Strona główna
@app.route('/')
def homepage():
    return render_template("homepage.html")


#Lista granych filmów
@app.route('/nowplaying/')
def nowplaying():
    selected_list = request.args.get("list_type","now_playing")
    if not selected_list:
        abort(404)
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("nowplaying.html", movies=movies, current_list=selected_list)


#Lista popularnych filmów
@app.route('/toprated/')
def toprated():
    selected_list = request.args.get("list_type","top_rated")
    if not selected_list:
        abort(404)
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("toprated.html", movies=movies, current_list=selected_list)


#Lista nadchodzących filmów
@app.route('/upcoming/')
def upcoming():
    selected_list = request.args.get("list_type","upcoming")
    if not selected_list:
        abort(404)
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("upcoming.html", movies=movies, current_list=selected_list)


#Lista popularnych filmów
@app.route('/popular/')
def popular():
    selected_list = request.args.get("list_type","popular")
    if not selected_list:
        abort(404)
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("popular.html", movies=movies, current_list=selected_list)


#Detale filmu
@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_image = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_image['backdrops'])
    if not details:
        abort(404)
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


#Wyszukiwarka
@app.route("/search")
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search(search_query=search_query)
    else:
        movies = []
    return render_template("search.html", movies=movies, search_query=search_query)


#Obecnie wyświetlanie filmy
@app.route("/today")
def today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("today.html", movies=movies, today=today)


#Dodawanie do ulubionych
@app.route("/favorites/add", methods=["POST"])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        FAVORITES.add(movie_id)
        flash(f'Added movie {movie_title} to favorites')
    return redirect(url_for('show_favorites'))


#Wyświetlenie ulubionych
@app.route("/favorites")
def show_favorites():
    if FAVORITES:
        movies = []
        for movie_id in FAVORITES:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("favorites.html", movies=movies)


#Obsługa błędów
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}),404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)






if __name__ == '__main__':
    app.run(debug=True)