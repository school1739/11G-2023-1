class Player:
    def __init__(self, name):
        print("Новый раб прибыл, милорд")
        self.name=name
    def say(self, message):
        print(message)
    def saytrue(self):
        self.say("Zhirinovsky was right")

Ivanov = Player("Ivanoff")
Petrov = Player("Petrosheves")

Ivanov.say("Готов вкалывать")
Petrov.say("Опять работа?")

Ivanov.saytrue()
print(Ivanov.name, "," ,Petrov.name)
Ivanov.say(Ivanov.name)