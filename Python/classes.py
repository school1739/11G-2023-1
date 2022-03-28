import random

"""
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
IvanovJr.sayShit()"""

"""class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    def get_name(self):  # Функция-геттер - NAME
        return self.__name

    def set_name(self, name):  # Функция-сеттер - NAME
        self.__name = name

    def get_age(self):  # Функция-геттер - AGE
        return self.__age

    def set_age(self, age):  # Функция-сеттер - AGE
        if 0 < age < 110:
            self.__age = age
        else:
            print("Are you fucked up, dude?")

    def get_info(self):  # Инфогеттер
        print(f"Name: {self.__name}, Age: {self.__age}")"""


class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    @property
    def name(self):  # Функция-геттер - NAME
        return self.__name

    @name.setter
    def name(self, name):  # Функция-сеттер - NAME
        last_name=self.__name
        self.__name = name
        print(f"{last_name} is now {self.__name}")

    @property
    def age(self):  # Функция-геттер - AGE
        return self.__age

    @age.setter
    def age(self, age):  # Функция-сеттер - AGE
        if 0 < age < 110:
            self.__age = age
        else:
            print("Are you fucked up, dude?")

    def get_info(self):  # Инфогеттер
        print(f"Name: {self.__name}, Age: {self.__age}")


Rick = Dude("Rick")
# Rick.get_info()
print(Rick.name)
Rick.name = "Dick"
print(Rick.name)
