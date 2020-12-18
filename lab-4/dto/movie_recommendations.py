# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MovieRecommendations:
    """
    Class to hold lists of recommended and not recommended movies.

    Attributes
    ----------
    must_watch : list
        list containing MovieInfo objects which one should watch
    avoid_movies : list
        list containing MovieInfo objects which one should not watch
    """
    def __init__(self, must_watch, avoid):
        """
        Creates all attributes needed for the MovieRecommendations object.

        Parameters
        ----------
        must_watch : list
            list containing MovieInfo objects which one should watch
        avoid_movies : list
            list containing MovieInfo objects which one should not watch
        """
        self.must_watch_movies = must_watch
        self.avoid_movies = avoid
