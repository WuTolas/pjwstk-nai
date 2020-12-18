# Movies recommendation engine
# Authors: Damian Rutkowski (s16583), Piotr Krajewski (s17410)
# Environment setup: https://github.com/WuTolas/pjwstk-nai/tree/main/lab-4/README.md

import scrapy
from .items import MovieItem
from inline_requests import inline_requests
from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess


class MovieSpider(scrapy.Spider):
    """
    Movie spider for parsing basic information about movies.

    Attributes
    ----------
    name : str
        name of the spider
    custom_settings : dict
        custom settings for the spider
    base_url : str
        base url of the site from which data will be parsed
    output : list
        list for holding parse result
    start_urls : list
        list for holding site urls to be parsed

    Methods
    -------
    parse(response):
        Parses information about movie and puts it into a list.
    crawl(title):
        Creates new Process in which crawling will be executed.
    execute_crawling(queue, data_arr, title):
        Executes crawling for movie spider, and puts the result in the queue.
    """
    name = 'moviespider'
    custom_settings = {
        'DOWNLOAD_DELAY': 0.02,
        'COOKIES_ENABLED': False
    }

    def __init__(self, title, output, **kwargs):
        """
        Constructs all the necessary attributes for the spider.

        Parameters
        ----------
        title : str
            title of the movie to be parsed
        output : list
            used for storing parse result
        """
        super().__init__(**kwargs)
        self.base_url = "https://www.filmweb.pl"
        query_part = "/search?q={title}"
        self.output = output
        self.start_urls.append(self.base_url + query_part.format(title=title))
    
    @inline_requests
    def parse(self, response):
        """
        Parses information about movie and puts it into a list.

        Parameters
        ----------
        response : Response
            response from the parsed site

        Returns
        -------
        None
        """
        href = response\
            .xpath("//div[@id='searchResult']/descendant::a[@class='poster__link'][1]/@href")\
            .get()
        if href is None:
            raise ValueError("Movie title is could not be found")

        movie_page = self.base_url + href
        movie_response = yield scrapy.Request(movie_page, dont_filter=True)

        movie = MovieItem()
        movie['rating'] = movie_response\
            .xpath("//span[@class='filmRating__rateValue'][1]/text()")\
            .get()
        movie['description'] = movie_response\
            .xpath("//div[@class='filmPosterSection__plot'][1]/text()")\
            .get()
        movie['genre'] = movie_response\
            .xpath("normalize-space(//div[contains(@class, 'filmInfo__header') and contains(text(), 'gatunek')][1]/following-sibling::div)")\
            .get()
        movie['production_country'] = movie_response\
            .xpath("normalize-space(//div[contains(@class, 'filmInfo__header') and contains(text(), 'produkcja')][1]/following-sibling::div)")\
            .get()
        self.output.append(movie)

    @staticmethod
    def crawl(title):
        """
        Creates new Process in which crawling will be executed.

        Parameters
        ----------  
        title : str
            title of the movie to be parsed
        
        Returns
        -------
        list
            contains one result (looks stupid - should be changed)
        """
        data_arr = []
        queue = Queue()
        p = Process(target=MovieSpider.execute_crawling, args=(queue, data_arr, title))
        p.start()
        p.join()
        return queue.get()

    @staticmethod
    def execute_crawling(queue, data_arr, title):
        """
        Executes crawling for movie spider, and puts the result in the queue.

        Parameters
        ----------
        queue : Queue
            queue in which final result will be stored and used to exchange objects between processes
        data_arr : list
            used to store result from the spider
        title : str
            title of the movie to be parsed
        
        Returns
        -------
        None
        """
        process = CrawlerProcess()
        process.crawl(MovieSpider, title=title, output=data_arr)
        process.start()
        if len(data_arr) == 0:
            queue.put(title)
        else:
            queue.put(data_arr[0])