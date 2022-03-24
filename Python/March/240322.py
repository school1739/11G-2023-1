import random
"""..."""

class Dude:
    def __init__(self, name):
        self.__name=name
        print(f"{self.__name} is born")
        self.__age=random.randint(0, 90)

def get_age(self):  # Функция-геттер для AGE
    return self.__age

def set_age(self, age): # Фунткция-сеттер для AGE
    if 0<age<110:
        self.__age=age
    else:
        print("Are you fucked up, dude?")

def get_name(self): # Функция-геттер для NAME
    return self.__name

def set_name(self, age): # Фунткция-сеттер для NAME
    pass

Rick = Dude("Rick")
Rick.get_info()