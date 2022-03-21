import random


def globalSay(msg):
    print(msg)


class Player_inCapsule:
    def __init__(self, name, age):
        print("Создан инкапуслированный игрок")
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


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")

print(f"Player name: {Ivanov.name}      Player age: {Ivanov.age}")
print(f"Player name: {Petrov.name}      Player age: {Petrov.age}")

Ivanov.name = "Was Ivanoff once"
Ivanov.age = 78

print()
print(f"Player name: {Ivanov.name}      Player age: {Ivanov.age}")

print()
Semenoff = Player_inCapsule("SemiOne", 55)

print(Semenoff.say_age())
print(Semenoff.say_name())