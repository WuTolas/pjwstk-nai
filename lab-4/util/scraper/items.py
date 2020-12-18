# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

import scrapy


class MovieItem(scrapy.Item):
    """
    Movie container which defines fields needed from the parsed data.

    Attributes
    ----------
    description : str
        description of the movie
    genre : str
        genre of the movie
    production_country : str
        country where it was produced
    rating : double
        site rating of the movie
    """
    description = scrapy.Field()
    genre = scrapy.Field()
    production_country = scrapy.Field()
    rating = scrapy.Field()