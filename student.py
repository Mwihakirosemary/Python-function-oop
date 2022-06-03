# class Student:
#     name = "Effence"
#     age  = 22
#     country = "Kenya"
#     school = "Akirachix"

from pytz import country_names


class Student:
    school = "Akirachix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age  = age
        self.country = country

    def greeting(self):
        return f"Hello {self.first_name} from {self.country} welcome to {self.school}"

    def full_name(self):
        return f"Hello {self.first_name} {self.last_name}"

    def year_of_birth(self):
        year = 2022 - self.age
        return f"Hello {self.first_name} from {self.last_name} you were born in" ,year

    def initials(self):
        return f"Hello {self.first_name[0]}{self.last_name[0]} welcome to {self.school}"
