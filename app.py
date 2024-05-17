from flask import Flask, request, jsonify, render_template
from chatbot import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    query = request.get_json()["query"]
    response = chatbot.respond(query)
    return jsonify(response)

@app.route("/movie_details", methods=["POST"])
def movie_details():
    imdb_id = request.get_json()["imdb_id"]
    details = chatbot.get_movie_details(imdb_id)
    return jsonify(details)

if __name__ == "__main__":
    app.run(debug=True)