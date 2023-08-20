"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
Section: CP164 B
__updated__ = "2023-01-11"
-------------------------------------------------------
"""
from Movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    # Your code here
    title =  input("Title:")
    year = int(input("Year of release:"))
    director = input("Director:")
    rating = float(input("Rating:"))
    genres = read_genres()
    
    
    #creating a movie object that has all the data
    movie = Movie(title,year,director,rating,genres)
    
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """
    

    # Your code here
    line = line.split("|")
  
    title = line[0]
    year = int(line[1])
    director = line[2]
    rating = float(line[3])
    genre = line[4].split(",")
    genres = []
    # range goes through the length of it and i is the index of each
    # append add i to each genre
    for i in range(len(genre)):
        genres.append(int(genre[i])) 
        
        
        
    
    movie = Movie(title,year,director,rating,genres)
    
    
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    movies = []
    line = fv.readline().strip("\n")
    while(line != ""):
        movie = read_movie(line)
        movies.append(movie)
        line = fv.readline().strip("\n")
    
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    # Your code here
    print(Movie.genres_menu())
    string = " "
    string_list = []
    value = True
    
    while(value):
        string = input(("Enter a genre number (ENTER to quit):"))
        
        if (string) == "":
            if len(string_list) > 0:
                value = False
            else:
                print("Error: must have at least one genre")
            
        
        elif string.isdigit()  == False:
            print("Error not a positive number")
            
        elif int(string) in string_list:
            print("genre already chosen")
            
        elif (int(string) > len(Movie.GENRES)):
            print(f"Error: input must be <= {Movie.GENRES}")
            
        
            
        elif string.isdigit():
            string_list.append(int(string))
        
            
        string_list.sort()
        
    genres = string_list      
    
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    # Your code here
    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)
            
  
    

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    
    rmovies = []
    # Your code here
    for movie in movies:
        if movie.rating >= rating:
            rmovies.append(movie)
            
    
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    # Your code here
    
    gmovies = []
    # Your code here
    for movie in movies:
        for genres in movie.genres:
            if genres ==  genre:
                gmovies.append(movie)
            
    
    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    # Your code here

    gmovies = []
    # Your code here
    # for each movie in the list movies
    for movie in movies:
        # for each genre in movies genres of that movie
        if movie.genres == genres:
            gmovies.append(movie)
            
    return gmovies

    
    


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """

    # Your code here
    # create an array with same number of positions of the length of movies genres
    # populate it with all zeros use genres constant
    counts = [0] * len(Movie.GENRES)
    # for each movie inside movies list
    for movie in movies:
        # check each genre in genre and append that genre index by 1 to its place in the list
        for genre in movie.genres:
            # adds each genre by one to that spot in this list 
            counts[genre] += 1
            
    # returning the count of the gnre
    return list(counts)
