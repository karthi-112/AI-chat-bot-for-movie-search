import langchain
from langchain.llms import OpenAI
from langchain.chains import RAGChain
from langchain.retrievers import SelfQueryingRetriever

llm = OpenAI("Your API Key")  #replace your API-KEY
retriever = SelfQueryingRetriever(llm, movie_db.search_movies)
chain = RAGChain(llm, retriever)