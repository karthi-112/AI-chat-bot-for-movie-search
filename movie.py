import os
import requests
from langchain.retriever import LangChainRetriever
from langchain.openai import OpenAIAdapter

class MovieRetriever(LangChainRetriever):
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.adapter = OpenAIAdapter(openai_api_key)

    def retrieve(self, input_text):
        # Generate a query using Open AI API
        query = self.adapter.generate_query(input_text, "movie search")

        # Search the movie database using the generated query
        movies = self.search_movies(query)

        return movies

    def search_movies(self, query):
        # Use the OMDB API to search for movies
        api_key = "YOUR_OMDB_API_KEY"
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={query}"
        response = requests.get(url)
        data = response.json()

        movies = []
        for movie in data["Search"]:
            movies.append({
                "title": movie["Title"],
                "thumbnail": movie["Poster"],
                "url": movie["imdbID"]
            })

        return movies
