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
ivanofJunior.sayShit()
