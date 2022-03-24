"""
import random


def globalSay(msg):
    print(msg)


class Player:
    def __init__(self, name):
        print("Конструктор создал игрока")
        self.name = name
        self.age = random.randint(12, 55)

    def say(self, message):
        print(message)

    def sayShit(self):
        self.say("Shit!")

    def sayGlobal(self):
        globalSay("Shit global")


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")

class playerJr(Player):
    def __init__(self, name):
        print("asdas")
        self.name=name

def study(self):
    print(self.name,"ботает в", self.school)

Ivanov = player("Ivanoff")
Petrov = player("P.E. Trove")
"""
import random

class Dude:
    def __init__(self, name):
        self.__name=name
        self.__age=random.randint(0, 90)

    def set_age(self, age):
        if 0<age<90:
            self.__age=age
        else:
            print("Are you fucked up, dude?")

    def show_age(self):
        return self.__age

    def say__name(self):
        return self.__name

    def show_all(self):
        print(f"Name:{self.__name}, Age: {self.age}")

