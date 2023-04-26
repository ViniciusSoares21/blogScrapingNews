from abc import ABC, abstractmethod


class Scraping(ABC):
    @classmethod
    @abstractmethod
    def get_news():
        raise NotImplementedError
