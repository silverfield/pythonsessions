__author__ = 'ferrard'

class AimsStudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def print_name(self):
        print(self.name)

    def award_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades)/len(self.grades)

