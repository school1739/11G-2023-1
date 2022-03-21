import random


def globalSay(msg):
    print(msg)


class Player_inCapsule:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say_name(self):
        return self.__name

    def say_age(self):
        return self.__age


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


class PlayerJr(Player):
    def __init__(self, name):
        print("Конструктор создал МИНИ игрока")
        self.name=name
        self.school="1739"

    def study(self):
        print(self.name, "ботает в", self.school)


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")
Sidorov = Player_inCapsule("Sidor OFF", 55)

IvanovJr = PlayerJr("Ivanoff Junior")
print(IvanovJr.name)

IvanovJr.study()
IvanovJr.sayShit()