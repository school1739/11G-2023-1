import random

"""
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
"""
class Dude:
    def __init__(self, name):
        self.__name= name
        self.__age=random.randit(0,90)

    def get_name(self): # функция-геттер -Name
        return self.__name

    def set_name(self, name):
        self.name=name

    def get_age(self): # функция-геттер- age
        return self.__age


    def set_age(self, age):
        if 0<age<110:
            self.__age=age
        else:
            print("Are yuo fucked up, dude?")

    def get_info(self):# инфогеттер
        print(f"Name: {self.__name,}")