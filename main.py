from flask import Flask, jsonify

app = Flask(__name__)

class Movie():
    def __init__(self, id, title, rating):
        self.id = id
        self.title = title
        self.rating = rating

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'rating': self.rating
        }

@app.route("/movies")
def hello_world():
    movies =  [Movie(1, 'Good fellas', 5), Movie(2, 'Mission Impossible', 4.8), Movie(3, 'Fast and Furious', 4.5)];
    return jsonify([x.serialize() for x in movies])