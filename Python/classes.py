import random


'''def globalSay(msg):
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
Sidorov.name="Sidoroff 228"'''


"""class Dude:
    def __init__(self, name):
        self.__name=name
        print(f"{self.__name} is born")
        self.__age=random.randint(0,90)
    def get__age(self):
        return self.__age
    def set_age(self, age):   #функция-сеттер
        if 0<age<90:
            self.__age=age
        else:
            print("Are you fcked up, Dude?")
    def get__name(self):
        return self.__name
    def set_name(self):
        return self.__name
Rick=Dude("Rick")
Rick.show__all"""


class Dude:
    def __init__(self, name):
        self.__name=name
        print(f"{self.__name} is born")
        self.__age=random.randint(0,90)
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):   #функция-сеттер
        if 0<age<90:
            self.__age=age
        else:
            print("Are you fcked up, Dude?")
    @name.setter
    def name(self):
        last_name=self.__name
        return self.__name
        print(f"{last_name}is now {self.__name}")
    @property
    def name(self, name):
        return self.__name
    def get_info(self):
        print(f'Name:{self.__name}, Age:{self.__age}')
Rick=Dude("Rick")
print(Rick.name)
Rick.name="Dick"
print(Rick.name)