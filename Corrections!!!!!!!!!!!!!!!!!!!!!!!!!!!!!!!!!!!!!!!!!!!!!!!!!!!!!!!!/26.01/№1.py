# Функция для расчета гипотенузы

def Gip(katet_1,katet_2):
    gip=(katet_1**2 + katet_2**2)**0.5
    print(round(gip,3))

Gip(int(input("Чему равен катет №1: ")),int(input("Чему равен катет №2: ")))