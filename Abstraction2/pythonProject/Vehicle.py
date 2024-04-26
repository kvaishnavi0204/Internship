from AbstractVechicle import AbstractVehicle


class Bike(AbstractVehicle):
    def display_details(self):
        print("Bike Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)


class Car(AbstractVehicle):
    def display_details(self):
        print("Car Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)


class Scooty(AbstractVehicle):
    def display_details(self):
        print("Scooty Details:")
        print("Color:", self.color)
        print("Number of Tyres:", self.num_tyres)
        print("Gears:", self.gears)
