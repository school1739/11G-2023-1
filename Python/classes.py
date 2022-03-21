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



