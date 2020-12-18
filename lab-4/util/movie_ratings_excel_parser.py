# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

from model.movie_person import MoviePerson
from model.movie_rating import MovieRating
import pandas as pd


class MovieRatingsExcelParser:
    """
    Utility class to parse people who rated movies from 1 to 10.

    Methods
    -------
    parse_from_xlsx(file_name)
        Static method to parse data from the excel file.
    """

    @staticmethod
    def parse_from_xlsx(file_name):
        """
        Parses data from the excel file (xlsx extension).

        Parameters
        ----------
        file_name : str

        Returns
        -------
        array[MoviePerson]
            1 dimensional array containing MoviePerson objects 
        """
        row_start = 0
        col_start = 0
        file = './' + file_name + '.xlsx'
        read_data = pd.read_excel(file, header=None, sheet_name='Ćwiczenia 04', index_col=None, dtype=str)
        for row in range(read_data.shape[0]):
            for col in range(read_data.shape[1]):
                if read_data.iat[row, col] == 'Osoba':
                    row_start = row + 1
                    col_start = col
                    break

        delete_mark = '123:a:345:b:678'
        sliced = read_data.loc[row_start:, col_start:].fillna(delete_mark)
        persons = []

        for row in sliced.values:
            j = 0
            while j < len(row):
                if row[j] is not delete_mark:
                    if j == 0:
                        first_name = row[j].split()[0]
                        last_name = row[j].split()[1]
                        person = MoviePerson(first_name, last_name)
                    else:
                        if j % 2 == 1:
                            title = str(row[j]).strip()
                            if len(title) < 2:
                                error_msg = 'Invalid movie title: ' + title + ' -> Looking for next record' 
                                print(error_msg)
                                j += 2
                                continue
                            if any(m.title == title for m in person.movie_ratings):
                                error_msg = 'Movie was already rated: ' + title + ' -> Looking for next record'
                                print(error_msg)
                                j += 2
                                continue
                        else:
                            try:
                                rating = int(row[j])
                                if rating < 1 or rating > 10:
                                    error_msg = 'Value in a cell is not within valid rating range (1 - 10) - could not add movie rating: ' + str(title) + ' : ' + str(rating)
                                    print(error_msg)
                                else:
                                    m_rating = MovieRating(title, rating)
                                    person.add_rating(m_rating)
                            except ValueError:
                                error_msg = 'Value in a cell is not a number - could not add movie rating: ' + str(title) + ' : ' + str(rating)
                                print(error_msg)
                else:
                    if j % 2 == 1:
                        j += 2
                        continue
                j += 1
            persons.append(person)
        
        return persons
