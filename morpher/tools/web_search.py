from langchain.utilities import GoogleSerperAPIWrapper


def web_search(input: str):
    search = GoogleSerperAPIWrapper()
    return search.run(input)

# TODO: implement web_crawler with browserless or something similar for in-depth searches
