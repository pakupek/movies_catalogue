from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/nowplaying/')
def nowplaying():
    selected_list = request.args.get("list_type","now_playing")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("nowplaying.html", movies=movies, current_list=selected_list)


@app.route('/toprated/')
def toprated():
    selected_list = request.args.get("list_type","top_rated")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("toprated.html", movies=movies, current_list=selected_list)


@app.route('/upcoming/')
def upcoming():
    selected_list = request.args.get("list_type","upcoming")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("upcoming.html", movies=movies, current_list=selected_list)


@app.route('/popular/')
def popular():
    selected_list = request.args.get("list_type","popular")
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("popular.html", movies=movies, current_list=selected_list)



@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_image = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_image['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


if __name__ == '__main__':
    app.run(debug=True)