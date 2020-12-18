# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MoviePersonScore:
    """
    Class to hold information about person movie ratings, common movies and similarity score.

    Attributes
    ----------
    movie_person : MoviePerson
    common_movies : list
        list containing CommonMovieRating objects
    similarity_score : double
        score between candidate (this movie_person) and analysed person

    Methods
    -------
    get_sorted_unique_movies_ratings(reversed=False):
        Generates unique (without common movies) list of movies which candidate watched compared to analysed person.
    """

    def __init__(self, movie_person, common_movies, similarity_score):
        """
        Creates all attributes needed for the MoviePersonScore object.

        Parameters
        ----------
        movie_person : MoviePerson
        common_movies : list
            list containing CommonMovieRating objects
        similarity_score : double
            score between candidate (this movie_person) and analysed person
        """
        self.movie_person = movie_person
        self.common_movies = common_movies
        self.similarity_score = similarity_score

    def get_sorted_unique_movies_ratings(self, reversed=False):
        """
        Generates unique (without common movies) list of movies which candidate watched compared to analysed person.
        List can be sorted in two ways - ascending or descending, based on reversed parameter.

        Parameters
        ----------
        reversed : boolean
            default false
        
        Returns
        -------
        list
            list containing unique movies with ratings (MovieRating objects)
        """
        movie_ratings = []
        for mr in self.movie_person.movie_ratings:
            if any(cm.title == mr.title for cm in self.common_movies):
                continue
            else:
                movie_ratings.append(mr)
        movie_ratings.sort(key=lambda mr: mr.rating, reverse=reversed)
        return movie_ratings
