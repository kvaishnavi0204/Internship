from python3 import AbstractFruits


class Mango(AbstractFruits):
    def display_details(self):
        print("Mango Details:")
        print("color:", self.color)
        print("season:", self.season)
        print("taste", self.taste)


class Apple(AbstractFruits):
    def display_details(self):
        print("Apple Details:")
        print("color:", self.color)
        print("season:", self.season)
        print("taste", self.taste)


class Orange(AbstractFruits):
    def display_details(self):
        print("Orange Details:")
        print("color:", self.color)
        print("season:", self.season)
        print("taste", self.taste)


class Watermelon(AbstractFruits):
    def display_details(self):
        print("Watermelon Details:")
        print("color:", self.color)
        print("season:", self.season)
        print("taste", self.taste)


class Grapes(AbstractFruits):
    def display_details(self):
        print("Grapes Details:")
        print("color:", self.color)
        print("season:", self.season)
        print("taste", self.taste)
