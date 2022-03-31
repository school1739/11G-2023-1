import random


class Human:
    def __init__(self, name):
        self.__name = name

    @property  # Аннотатор
    def name(self):
        return self.__name

    def get_info(self):
        print(f"Name: {self.__name}")


class Employee(Human):
    def __init__(self, name, company):
        # self.__name = name
        super().__init__(name)
        self.company = company

    def work(self):
        print(f"{self.name} works somewhere")

    def get_info(self):
        super().get_info()
        print(f"Company: {self.company}")


Rick = Human("Rick")
print(Rick.name)
Rick.get_info()

Dick = Employee("Dick", 'Microsoft')
print(Dick.name)
Dick.get_info()
