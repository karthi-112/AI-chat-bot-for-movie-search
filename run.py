import json
import os
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Load movie data
with open("movies.json", "r") as f:
    movies = json.load(f)

# Prepare metadata
metadata = [
    {
        "title": movie["title"],
        "year": movie["year"],
        "genre": movie["genre"],
        "rating": movie["rating"],
        "thumbnail": movie["thumbnail"],
    }
    for movie in movies
]

# Prepare embeddings
embeddings = OpenAIEmbeddings()

# Create vector database
db_settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="vector_db",
)
vector_db = Chroma(
    embedding_function=embeddings.embed_query,
    collection_name="movies",
    settings=db_settings,
)

# Ingest documents
vector_db.add_documents(movies, metadatas=metadata)