from ..movie import *

def titles(movies):
    return [movie.title for movie in movies]

print(titles(movies))