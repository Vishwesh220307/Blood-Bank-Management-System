from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, person_id, name, age, gender, mobile_number):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number

    @abstractmethod
    def display_details(self):
        pass

    def update_details(self, name, age, gender, mobile_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number