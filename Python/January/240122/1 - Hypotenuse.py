"""Напишите функцию, принимающую на вход длины двух катетов прямо-
угольного треугольника и возвращающую длину гипотенузы, рассчитан-
ную по теореме Пифагора. В главной программе должен осуществляться
запрос длин сторон у пользователя, вызов функции и вывод на экран
полученного результата."""
import math


# подсчет гипотенузы
def hypotenuse(first_cathetus, second_cathetus):
    hypotenuse1 = math.sqrt(first_cathetus ** 2 + second_cathetus ** 2)
    return hypotenuse1


# вызов функции и округление значения гипотенузы
length_of_hypotenuse = round(hypotenuse(first_cathetus=int(input("length of first cathetus: ")),
                                        second_cathetus=int(input("length of second cathetus: "))), 2)

# длина гипотенузы
print("length of hypotenuse is", length_of_hypotenuse)
