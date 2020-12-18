# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MovieInfo:
    """
    Class to hold information about movie.

    Attributes
    ----------
    title : str
    site_rating : double
    description : str
    genre : str
    production_country : str
    """

    def __init__(self, title, site_rating, description, genre, production_country):
        """
        Creates all attributes needed for the MovieInfo object.

        Parameters
        ----------
        title : str
        site_rating : double
        description : str
        genre : str
        production_country : str
        """
        self.title = title
        self.site_rating = site_rating
        self.description = description
        self.genre = genre
        self.production_country = production_country
