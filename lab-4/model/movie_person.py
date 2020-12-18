# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MoviePerson:
    """
    Class to represent person who is connected to the movies, through given ratings.

    Attributes
    ----------
    first_name : str
    last_name : str
    movie_ratings : list
        list containing MovieRating objects
    
    Methods
    -------
    add_rating(movie_rating):
        Adds movie rating to the movie ratings array.
    """

    def __init__(self, first_name, last_name):
        """
        Creates all attributes needed for the MoviePerson object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.movie_ratings = []
        
    def add_rating(self, movie_rating):
        """
        Adds movie rating to the movie ratings array.

        Parameters
        ----------
        movie_rating : MovieRating

        Returns
        -------
        None
        """
        self.movie_ratings.append(movie_rating)
