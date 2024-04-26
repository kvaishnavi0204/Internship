from abc import ABC


class AbstractVehicle(ABC):
    def __init__(self, color, num_tyres, gears):
        self.color = color
        self.num_tyres = num_tyres
        self.gears = gears

    def display_details(self):
        pass
