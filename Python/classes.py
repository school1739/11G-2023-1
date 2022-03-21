import random


def globalSay(msg):
    print(msg)


class Player in Capsul:
    def __init__(self, name, age):
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
Sidorov = Player_inCapsul("Sidorof OFF", 55)

print(Sidorov.name)
Sidorov.name="Sidoroff 228"
