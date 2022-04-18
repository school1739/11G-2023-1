"""class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    def get_name(self):
        return self.__name

    def set_name(self):
        self.__name

    def get_age(self): # Функцмя геттер
        return self.__age

    def set_age(self, age): # Функция сеттер
        if 0 < age < 90:
            self.__age = age
        else:
            print("Are you dummy?")

    def get_info(self): # Инфогетер
        print(f'Name: {self.__name}, Age: {self.__age}')




Rick = Dude("Rick")
Rick.show_all()"""

"""def globalSay(msg):
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


class PlayerJr(Player):
    def __init__(self, name):
        print("Конструктор создал МИНИ игрока")
        self.name=name
        self.school="1739"

    def study(self):
        print(self.name, "ботает в", self.school)


Ivanov = Player("Ivanoff")
Petrov = Player("P.E. Trove")
Sidorov = Player_inCapsule("Sidor OFF", 55)

IvanovJr = PlayerJr("Ivanoff Junior")
print(IvanovJr.name)

IvanovJr.study()
IvanovJr.sayShit()"""

"""class Dude:
    def __init__(self, name):
        self.__name = name
        print(f"{self.__name} is born")
        self.__age = random.randint(0, 90)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self):
        self.__name

    @property
    def age(self): # Функцмя геттер
        return self.__age

    @name.setter
    def age(self, age): # Функция сеттер
        if 0 < age < 90:
            self.__age = age
        else:
            print("Are you dummy?")

    def get_info(self): # Инфогетер
        print(f'Name: {self.__name}, Age: {self.__age}')

Rick = Dude("Rick")
print(Rick.name)"""

"""class Human:
    def __init__(self, name):
        self.__name = name

    @property  # Аннотатор
    def name(self):
        return self.__name

    def get_info(self):
        print(f"Name: {self.__name}")


class Employee(Human):
    def __init__(self, name, company):
        super().__init__(name)
        self.__company = company

    def work(self):
        print(f"{self.__name} works somewhere")

    def get_info(self):
        super().get_info()
        print(f"Company: {self.__company}")

Rick=Human("Rick")
print(Rick.name)
Rick.get_info

Dick=Employee("Dick", "Microsoft")
print(Dick.name)"""
