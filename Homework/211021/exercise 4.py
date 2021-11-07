print("Введите дату рождения")
a= int(input("День "))
b= int(input("Месяц "))
c= int(input("Год "))
if 20<a<=31 and b==3 or 1<=a<20 and b==4:
    print("Овен")
elif 19<a<=30 and b==4 or 1<=a<21 and b==5:
    print("Телец")
elif 20<a<=31 and b==5 or 1<=a<21 and b==6:
    print("Близнецы")
elif 20<a<=30 and b==6 or 1<=a<23 and b==7:
    print("Рак")
elif  22<a<=31 and b==7 or 1<=a<23 and b==8:
    print("Лев")
elif 22<a<=31 and b==8 or 1<=a<23 and b==9:
    print("Дева")
elif 22<a<=30 and b==9 or 1<=a<23 and b==10:
    print("Весы")
elif 22<a<=31 and b==10 or 1<=a<22 and b==11:
    print("Скорпион")
elif 21<a<=30 and b==11 or 1<=a<22 and b==12:
    print("Стрелец")
elif 21<a<=31 and b==12 or 1<=a<20 and b==1:
    print("Козерог")
elif 19<a<=31 and b==1 or 1<=a<19 and b==2:
    print("Водолей")
elif 18<a<=29 and b==2 or 1<=a<21 and b==3:
    print("Рыбы")
if c%12==8:
    print("Дракон")
elif c%12==9:
    print("Змея")
elif c%12==10:
    print("Лощадь")
elif c%12==11:
    print("Коза")
elif c%12==0:
    print("Обезьяна")
elif c%12==1:
    print("Петух")
elif c%12==2:
    print("Собака")
elif c%12==3:
    print("Свинья")
elif c%12==4:
    print("Крыса")
elif c%12==5:
    print("Бык")
elif c%12==6:
    print("Тигр")
elif c%12==7:
    print("Кролик")
