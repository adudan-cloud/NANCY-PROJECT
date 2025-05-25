class Car:
    # class variable
    num_wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model} with {Car.num_wheels} wheels"

    @classmethod
    def change_wheel_count(cls, new_count):
        cls.num_wheels = new_count 


class Dog:
    # class variable
    species = "canis lupus familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

    @classmethod
    def get_species(cls):
        return cls.species


class Student:
    # class variable
    school_name = "kiti school"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Grade: {self.grade}, School: {self.school_name}"

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school




    