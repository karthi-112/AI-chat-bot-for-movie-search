import langchain
from langchain.llms import OpenAI
from langchain.chains import RAGChain
from langchain.retrievers import SelfQueryingRetriever

llm = OpenAI("sk-proj-ukB39fA9pe5ohn4VXIPnT3BlbkFJ3ERSTE5C6uQHCmTdcOgZ")
retriever = SelfQueryingRetriever(llm, movie_db.search_movies)
chain = RAGChain(llm, retriever)