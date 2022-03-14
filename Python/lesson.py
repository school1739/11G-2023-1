import random


class Player:
    def __init__(self, name):
        print("Консструктор создал игрока")
        self.name = name
        self.age = random.randint(12, 55)

    def say(self, message):
        print(message)

    def say_shit(self):
        # print("shit")
        self.say("shit")


ivanow = Player("ivan")

ivanow.say(ivanow.name)
# print(ivanow.name)

ivanow.say(ivanow.age)
# ivanow.say("Ivan")
# ivanow.say_shit()

ivanow.work = "school"
ivanow.say(ivanow.work)
