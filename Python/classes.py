import random

"""def globalSay(msg):
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


#
# Ivanov = Player("Ivanoff")
# Petrov = Player("P.E. Trove")

# sidorov = Player_inCapsule("sidorov", -43)
# # sidorov.name="Ivan"
# print(sidorov.say_age())


class playerJunior(Player):
    def __init__(self, name):
        print("Создал МИНИ игрока")
        self.name = name
        self.school = "1739"

    def study(self):
        print(self.name, "WORK!", self.school)


ivanofJunior = playerJunior("Ivan")
ivanofJunior.study()
ivanofJunior.sayShit()"""

"""class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    def get_name(self):  # Функция-геттер NAME
        return self.__name

    def set_name(self, name):  # Функция-сеттер NAME
        self.__name = name

    def get_age(self):  # Функция-геттер AGE
        return self.__age

    def set_age(self, age):  # Функция-сеттер AGE
        if 0 < age < 90:
            self.__age = age
        else:
            print("No, dumbass")

    def get_info(self):  # Функция-инфогеттер
        print(f"Name: {self.__name}, Age: {self.__age}")"""


class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    @property
    def name(self):  # Функция-геттер NAME
        return self.__name

    @name.setter
    def name(self, name):  # Функция-сеттер NAME
        last_name = self.__name
        self.__name = name
        print(f"Last name is {last_name}")
    @property
    def age(self):  # Функция-геттер AGE
        return self.__age

    @age.setter
    def age(self, age):  # Функция-сеттер AGE
        if 0 < age < 90:
            self.__age = age
        else:
            print("No, dumbass")

    def get_info(self):  # Функция-инфогеттер
        print(f"Name: {self.__name}, Age: {self.__age}")


Rick = Dude("Rick")
# Rick.age()
# Rick.set_age(23)
# print(Rick.get_age())
print(Rick.name)
Rick.name = "dick"
print(Rick.name)
