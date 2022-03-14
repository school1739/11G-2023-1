class Player:
    def __init__(self):
        print("Конструктор создал игрока")
    def say(self):
        print("some shit")
    def sayShit(self):
        self.say("Shit")

Ivanov = Player()
Petrov = Player()

Ivanov.say()
Petrov.say()
Ivanov.sayShit()


