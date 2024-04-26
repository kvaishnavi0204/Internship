from abc import ABC, abstractmethod


class AbstractFruits(ABC):
    def __init__(self, color, season, taste):
        self.color = color
        self.season = season
        self.taste = taste

    @abstractmethod
    def display_details(self):
        pass
