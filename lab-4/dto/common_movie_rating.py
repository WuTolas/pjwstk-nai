# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class CommonMovieRating:
    """
    Class to represent common movie ratings between 2 people.

    Attributes
    ----------
    title : str
    rating1 : int
        rating of the first person
    rating2 : int
        rating of the second person
    """
    def __init__(self, title, rating1, rating2):
        """
        Creates attributes for holding information about common movies.
        """
        self.title = title
        self.rating1 = rating1
        self.rating2 = rating2
