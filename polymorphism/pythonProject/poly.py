class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

class Cow(Animal):
    def speak(self):
        return "moo!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat =Cat()
cow = Cow()

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(cow)

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def __add__(self, other):
       return f"{self.real+other.real}+{self.imaginary+self.imaginary}i"

c1=ComplexNumber(2,2)
c2=ComplexNumber(3,4)
print(c1+c2)

class Location:
    def __init__(self,loc1,loc2):
        self.loc1=loc1
        self.loc2=loc2

    def __eq__(self, other):
        if self.loc1 == other.loc2:
           return True
        else:
           return False

l1=(123456-19113)
l2=(64384-76338)
l3=(98366.0)
print(l1+l2/2)



