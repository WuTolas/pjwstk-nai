# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MovieRating:
    """
    Class to represent movie rating data.

    Attributes
    ----------
    title : str
        title of the movie (actually title would be more suitable here)
    rating : int
        rating of the movie - from 1 to 10
    """

    def __init__(self, title, rating):
        """
        Creates all attributes needed for the MovieRating object.
        """
        self.title = title
        self.rating = rating
