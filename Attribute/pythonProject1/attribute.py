class Student:
    def __init__(self, name, roll_number, password):
        self.name = name
        self._roll_number = roll_number
        self.__password = password

    def display_details(self):
        print("name:", self.name)
        print("roll_number:", self._roll_number)
        print("password:", self.__password)

    def password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


student = Student("vaishu", "22", "secure_password")
print("name(Public):", student.name)
print("roll_number(Protected):", student._roll_number)
print("password(Private):", student.password())

student.set_password("new_password")
student.display_details()