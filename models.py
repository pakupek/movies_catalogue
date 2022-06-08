import json

class Movie:
    def __init__(self):
        try:
            with open("movies.json", "r", encoding="utf-8") as f:
                self.movie = json.load(f)
        except FileNotFoundError:
            self.movie = []

    def all(self):
        return self.movie