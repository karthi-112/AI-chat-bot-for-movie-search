from rag_system import chain

class MovieChatbot:
    def __init__(self):
        self.chain = chain

    def respond(self, query):
        output = self.chain.generate(query)
        return self.format_output(output)

    def format_output(self, output):
        movies = []
        for item in output:
            title = item["title"]
            thumbnail = item["poster"]
            url = item["imdbID"]
            movies.append({"title": title, "thumbnail": thumbnail, "url": url})
        return movies

chatbot = MovieChatbot()