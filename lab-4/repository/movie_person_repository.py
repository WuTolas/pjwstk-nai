# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

class MoviePersonRepository:
    """
    Class for holding data about MoviePerson. Imitates database.

    Attributes
    ----------
    __movie_persons : list
        list containing MoviePerson objects

    Methods
    -------
    save_all(movie_persons):
        Saves all MoviePerson objects to the array.
    find_movie_person(first_name, last_name):
        Searches for provided person.
    find_all():
        Returns whole array containing MoviePersons objects.
    """

    def __init__(self):
        """
        Creates attributes needed for the MoviePersonRepository object.
        """
        self.__movie_persons = []

    def save_all(self, movie_persons):
        """
        Saves all MoviePerson objects to the array.

        Attributes
        ----------
        movie_persons : array[MoviePerson]
            1 dimensional array containing MoviePerson objects
        
        Returns
        -------
        None
        """
        self.__movie_persons = movie_persons

    def find_movie_person(self, first_name, last_name):
        """
        Searches for provided person. This kind of method would be terrible if there were more than 1 person with the same first name and last name.
        For current studies task - it's enough.

        Attributes
        ----------
        first_name : str
        last_name : str

        Returns
        -------
        MoviePerson
            when there is a match
        None
            when there is no such person
        """
        for mp in self.__movie_persons:
            if mp.first_name == first_name and mp.last_name == last_name:
                return mp
        return None

    def find_all(self):
        """
        Returns whole array containing MoviePersons objects.

        Returns
        -------
        list
            containing MoviePerson objects
        """
        return self.__movie_persons
