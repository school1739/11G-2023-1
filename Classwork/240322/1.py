from random import random


class Dude:
    def __init__(self,name):
        self._name = name
        self._age = random.randit(0,90)
    @name.setter
    def name(self):
        return self._age
    def set_name(self):
        return self._name
        self._age = age
    @property
    def age(self,age):
        if 0 < age <110:
            self._age = age
        else:
            print("Are you fucked up,dude?")
    def get_info(self):
        print(f"Name: {self._name}Age._name")
Rick=Dude("Rick")
Rick.get_info()








