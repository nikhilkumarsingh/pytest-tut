from datetime import datetime


class Student:

    def __init__(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = 0

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits
