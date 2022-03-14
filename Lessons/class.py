class Player:
    def __init__(self,name):
        print("sozdal")
        self.name=name
    def say(self,message):
        print(message)
    def sayshit(self):
        self.say("shit")
ivanov = Player("preok")
petrov = Player("gfjigf")
ivanov.say("z utq")
ivanov.sayshit()
print(ivanov.name,petrov.name)
ivanov.say(ivanov.name)