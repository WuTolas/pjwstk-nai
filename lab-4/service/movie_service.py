# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

import os
import sys
from repository.movie_person_repository import MoviePersonRepository
from dto.common_movie_rating import CommonMovieRating
from dto.movie_person_score import MoviePersonScore
from dto.movie_recommendations import MovieRecommendations
from dto.movie_info import MovieInfo
from util.scraper.movie_spider import MovieSpider
import numpy as np


class MovieService:
    """
    Movie service containing core logic for our movies recommendation engine.

    Attributes
    ----------
    __movie_person_repository : MoviePersonRepository
        imitates repository
    __positive_strong_correlation : double
        determines from which value two 'variables' are considered strong
    __minimum_rated_movies : int
        minimum amount of rated movies by one person needed to be considered as a (more or less) 'good' candidate for recommendations
    __minimum_common_movies : int
        minimum amount of common movies between candidate and analysed person needed to be considered as a (more or less) 'good' candidate for recommendations
    __recommendations_count : int
        exact amount of the recommendations (separately positive and negative) which enging will be aiming for
    __minimum_positive_rating_recommendation : int
        value from which particular movie rating will be considered as a positive recommendation
    __maximum_negative_rating_recommendation : int
        value to which particular movie rating will be considered as a negative recommendation

    Methods
    -------
    save_all(movie_person):
        Saves all MoviePerson objects in the repository.
    recommend_movies(full_name):
        Gets movie recommendations for given person. Might as well return object which is going to contain empty lists - depends if for particular
        person and requirements set in this class, recommendations will or will not be found.
    __get_movie_data(title):
        Gets data about movie.
    __get_positive_recommendations(people_scores):
        Creates list of movies which might be liked by analysed person.
    __get_negative_recommendations(people_scores):
        Creates list of movies which probably won't be liked by analysed person.
    __find_strongly_correlated_people(target):
        Looks for strongly correlated people for analysed person.
    __pearson_score(common_movie_ratings):
        Calculates pearson score between two people based on the rated common movies.
        Major part of this method's code is from: `Artificial Intelligence with Python` By Prateek Joshi
    __find_common_movies(movie_person1, movie_person2):
        Looks for common movies between analysed person (movie_person1) and candidate (movie_person2).
    find_movie_person(full_name):
        Searches for MoviePerson in the MoviePersonRepository.
        Prepares data before calling repository method.
    """

    def __init__(self):
        """
        Creates all attributes needed for the MovieService object.
        Instantiates MoviePersonRepository.
        """
        self.__movie_person_repository = MoviePersonRepository()
        self.__positive_strong_correlation = 0.7
        self.__minimum_rated_movies = 16
        self.__minimum_common_movies = 4
        self.__recommendations_count = 6
        self.__minimum_positive_rating_recommendation = 8
        self.__maximum_negative_rating_recommendation = 3
    
    def save_all(self, movie_persons):
        """
        Saves all MoviePerson objects in the repository.

        Parameters
        ----------
        movie_persons : array[MoviePerson]
            array containing MoviePerson objects

        Returns
        -------
        None
        """
        self.__movie_person_repository.save_all(movie_persons)
    
    def recommend_movies(self, full_name):
        """
        Gets movie recommendations for given person. Might as well return object which is going to contain empty lists - depends if for particular
        person and requirements set in this class, recommendations will or will not be found.

        Parameters
        ----------
        full_name : str
            first name and last name of the person
        
        Returns
        -------
        MovieRecommendations
        """
        target = self.find_movie_person(full_name)
        people_scores = self.__find_strongly_correlated_people(target)
        positive_recommendations = []
        negative_recommendations = []
        for title in self.__get_positive_recommendations(people_scores):
            positive_recommendations.append(self.__get_movie_data(title))
        for title in self.__get_negative_recommendations(people_scores):
            negative_recommendations.append(self.__get_movie_data(title))
        return MovieRecommendations(positive_recommendations, negative_recommendations)
    
    def __get_movie_data(self, title):
        """
        Gets data about movie.

        Parameters
        ----------
        title: str

        Returns
        -------
        MovieInfo
        """
        data = MovieSpider.crawl(title)
        if data == title:
            movie = MovieInfo(title, "", "", "", "")
        else:
            movie = MovieInfo(title, data['rating'], data['description'], data['genre'], data['production_country'])
        return movie

    def __get_positive_recommendations(self, people_scores):
        """
        Creates list of movies which might be liked by analysed person.
        
        Parameters
        ----------
        people_scores : list
            list containing MoviePersonScore objects

        Returns
        -------
        list
            list containing movie titles
        """
        positive_recommendations = []
        for p in people_scores:
            if p.similarity_score > 0:
                movies_ratings = p.get_sorted_unique_movies_ratings(True)
            else:
                movies_ratings = p.get_sorted_unique_movies_ratings()
            for mr in movies_ratings:
                if len(positive_recommendations) < 6 and not mr.title in positive_recommendations:
                    if p.similarity_score >= self.__positive_strong_correlation and mr.rating >= self.__minimum_positive_rating_recommendation:
                        positive_recommendations.append(mr.title)
                    elif p.similarity_score <= (self.__positive_strong_correlation * -1) and mr.rating <= self.__maximum_negative_rating_recommendation:
                        positive_recommendations.append(mr.title)
                elif len(positive_recommendations) == 6:
                    return positive_recommendations
        return positive_recommendations

    def __get_negative_recommendations(self, people_scores):
        """
        Creates list of movies which probably won't be liked by analysed person.
        
        Parameters
        ----------
        people_scores : list
            list containing MoviePersonScore objects

        Returns
        -------
        list
            list containing movie titles
        """
        negative_recommendations = []
        for p in people_scores:
            if p.similarity_score > 0:
                movies_ratings = p.get_sorted_unique_movies_ratings()
            else:
                movies_ratings = p.get_sorted_unique_movies_ratings(True)
            for mr in movies_ratings:
                if len(negative_recommendations) < 6 and not mr.title in negative_recommendations:
                    if p.similarity_score >= self.__positive_strong_correlation and mr.rating <= self.__maximum_negative_rating_recommendation:
                        negative_recommendations.append(mr.title)
                    elif p.similarity_score <= (self.__positive_strong_correlation * -1) and mr.rating >= self.__minimum_positive_rating_recommendation:
                        negative_recommendations.append(mr.title)
                elif len(negative_recommendations) == 6:
                    return negative_recommendations
        return negative_recommendations  

    def __find_strongly_correlated_people(self, target):
        """
        Looks for strongly correlated people for analysed person.

        Parameters
        ----------
        target : MoviePerson
            analysed person

        Returns
        -------
        list
            list containing MoviePersonScore objects in descending order (by score)
        """
        all_persons = self.__movie_person_repository.find_all()
        people_scores = []
        for person in all_persons:
            if target.first_name != person.first_name and target.last_name != person.last_name and len(person.movie_ratings) >= self.__minimum_rated_movies:
                common_movies = self.__find_common_movies(target, person)
                if len(common_movies) < self.__minimum_common_movies:
                    continue
                score = self.__pearson_score(common_movies)
                if (self.__positive_strong_correlation * -1) < score < self.__positive_strong_correlation:
                    continue 
                people_scores.append(MoviePersonScore(person, common_movies, score))
        people_scores.sort(key=lambda mps: mps.similarity_score, reverse=True)
        return people_scores

    def __pearson_score(self, common_movie_ratings):
        """
        Calculates pearson score between two people based on the rated common movies.
        Major part of this method's code is from: `Artificial Intelligence with Python` By Prateek Joshi

        Parameters
        ----------
        movie_person1 : MoviePerson
            analysed person
        movie_person2 : MoviePerson
            candidate for similar movie tastes

        Returns
        -------
        double
            or 0 when there is no correlation
        """
        ratings_count = len(common_movie_ratings)
        if ratings_count == 0:
            return 0

        person1_sum = np.sum([movie_rating.rating1 for movie_rating in common_movie_ratings])
        person2_sum = np.sum([movie_rating.rating2 for movie_rating in common_movie_ratings])

        person1_squared_sum = np.sum([np.square(movie_rating.rating1) for movie_rating in common_movie_ratings])
        person2_squared_sum = np.sum([np.square(movie_rating.rating2) for movie_rating in common_movie_ratings])

        sum_of_products = np.sum([movie_rating.rating1 * movie_rating.rating2 for movie_rating in common_movie_ratings])

        Sxy = sum_of_products - (person1_sum * person2_sum / ratings_count)
        Sxx = person1_squared_sum - np.square(person1_sum) / ratings_count
        Syy = person2_squared_sum - np.square(person2_sum) / ratings_count

        if Sxx * Syy == 0:
            return 0
        return Sxy / np.sqrt(Sxx * Syy)

    def __find_common_movies(self, movie_person1, movie_person2):
        """
        Looks for common movies between analysed person (movie_person1) and candidate (movie_person2).

        Parameters
        ----------
        movie_person1 : MoviePerson
            analysed person
        movie_person2 : MoviePerson
            candidate for similar movie tastes
        
        Returns
        -------
        list
            list containing CommonMovieRating objects
        """
        common_movie_ratings = []
        for movie1_rating in movie_person1.movie_ratings:
            movie2_rating = next((movie2_rating for movie2_rating in movie_person2.movie_ratings if movie2_rating.title == movie1_rating.title), None)
            if movie2_rating is not None:
                common_movie = CommonMovieRating(movie1_rating.title, movie1_rating.rating, movie2_rating.rating)
                common_movie_ratings.append(common_movie)
        return common_movie_ratings

    def find_movie_person(self, full_name):
        """
        Searches for MoviePerson in the MoviePersonRepository.
        Prepares data before calling repository method.

        Parameters
        ----------
        full_name : str
        
        Returns
        -------
        MoviePerson
            if exists in repository

        Raises
        ------
        TypeError
            when provided full name is incorrect (e.g. contains only first name)
        ValueError
            when person does not exist
        """
        full_name_arr = full_name.split(" ", 1)
        if len(full_name_arr) != 2:
            error_msg = 'Provided full name should contain first name and last name separated with spaces. Current value: ' + full_name
            raise TypeError(error_msg)
        movie_person = self.__movie_person_repository.find_movie_person(full_name_arr[0].strip(), full_name_arr[1].strip())
        if movie_person is None:
            error_msg = 'Provided person does not exist: ' + full_name
            raise ValueError(error_msg)
        return movie_person
