from flask import Flask
import csv 
all_movies = []
with open("Movie Data.csv") as m:
    reader = csv.reader(m)
    data = list(reader)
    all_movies = data[1:]
liked_movies = []
not_liked_movies = []
did_not_watch = []
app = flask(__name__)
@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })
@app.route("/liked_movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }),201
@app.route("/unliked_movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }),201
@app.route("/did_not_watch", methods = ["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }),201
if __name__ == "__main__":
    app.run()