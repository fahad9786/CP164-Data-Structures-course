"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
from Movie import Movie
from Movie_utilities import get_by_year, read_movies



movies = [Movie("Movie1", 2020, "Director1", 5, [1, 2, 3]),
          Movie("Movie2", 2019, "Director2", 7, [4, 2, 3]),
          Movie("Movie3", 2020, "Director3", 6, [1, 3]),
          Movie("Movie4", 2010, "Director4", 9, [2, 3]),
          Movie("Movie5", 2019, "Director5", 2, [3, 4, 5]),
          Movie("Movie6", 2018, "Director6", 4, [1, 4, 5])]
year = 2019

x = get_by_year(movies, year)
for f in x:
    print(f)