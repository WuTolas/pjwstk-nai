# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

from util.movie_ratings_excel_parser import MovieRatingsExcelParser
from service.movie_service import MovieService
from model.movie_person import MoviePerson
from model.movie_rating import MovieRating 


def main():
    """
    Program main method.
    """
    movie_persons = MovieRatingsExcelParser.parse_from_xlsx('movies')
    movie_service = MovieService()
    movie_service.save_all(movie_persons)

    print("People for who you can check recommendations:")
    for mp in movie_persons:
        print(mp.first_name + " " + mp.last_name)

    full_name = str(input("Type full name of the person you want to see movie recommendations: "))
    recommendations = movie_service.recommend_movies(full_name)

    print_headline(full_name)

    if len(recommendations.must_watch_movies) == 0 and len(recommendations.avoid_movies) == 0:
        print_headline("Looks like there is not enough data about this person to generate recommendations :(") 
    else:
        print_headline("YOU SHOULD CHECK THESE MOVIES:")
        for m in recommendations.must_watch_movies:
            print("-------------------------------------------------")
            print_movie(m)
            print("-------------------------------------------------")

        print_headline("AND BETTER AVOID THESE MOVIES:")
        for m in recommendations.avoid_movies:
            print("-------------------------------------------------")
            print_movie(m)
            print("-------------------------------------------------")


def print_movie(movie_info):
    """
    Prints data about movie.

    Parameters
    ----------
    movie_info : str
        MovieInfo object
    
    Returns
    -------
    None
    """
    print("Title: " + movie_info.title)
    print("Site rating: " + str(movie_info.site_rating))
    print("Description: " + str(movie_info.description))
    print("Genre: " + str(movie_info.genre))
    print("Production: " + str(movie_info.production_country))


def print_headline(message):
    """
    Prints the headline.

    Parameters
    ----------
    message : str
    """
    print("**************************************************************************************************************************************")
    print("*************************************************** " + message + " ***************************************************")
    print("**************************************************************************************************************************************")


if __name__ == "__main__":
    main()
