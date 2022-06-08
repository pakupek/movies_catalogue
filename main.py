from flask import Flask, render_template
import json
import requests
import tmdb_client

app = Flask(__name__)



@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}


@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=4)
    return render_template("homepage.html", movies=movies)




if __name__ == '__main__':
    app.run(debug=True)