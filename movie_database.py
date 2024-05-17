import requests

class MovieDatabase:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_movies(self, query):
        url = f"http://www.omdbapi.com/?apikey={self.api_key}&s={query}"
        response = requests.get(url)
        data = response.json()
        return data["Search"]

# Replace with your OMDb API key
api_key = "sk-proj-ukB39fA9pe5ohn4VXIPnT3BlbkFJ3ERSTE5C6uQHCmTdcOgZ"
movie_db = MovieDatabase(api_key)