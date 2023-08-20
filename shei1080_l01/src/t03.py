"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-01-18"
-------------------------------------------------------
"""


from Movie_utilities import Movie, read_movies

filename = "movies.txt"
file = open(filename,"r",encoding = "utf-8")

movies = read_movies(file)
for movie in movies:
    print(movie)


file.close()