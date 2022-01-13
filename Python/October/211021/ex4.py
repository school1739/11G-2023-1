day = int(input("Введите день своего рождения: "))
month = int(input("Введите месяц своего рождения (число): "))
year = int(input("Введите год своего рождения: "))

# определение по гороскопу

if (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and month == 1):
    print("По гороскопу вы Козерог")

elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
    print("По гороскопу вы Водолей")

elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
    print("По гороскопу вы Рыбы")

elif (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
    print("По гороскопу вы Овен")

elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
    print("По гороскопу вы Телец")

elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and month == 6):
    print("По гороскопу вы Близнецы")

elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
    print("По гороскопу вы Рак")

elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
    print("По гороскопу вы Лев")

elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and month == 9):
    print("По гороскопу вы Дева")

elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
    print("По гороскопу вы Весы")

elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and month == 11):
    print("По гороскопу вы Скорпион")

elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
    print("По гороскопу вы Стрелец")
else:
    print("неправильно введена дата, или родители врали вам о дате рождения и вы нематериален")

# определение животного по китайскому календарю

china = {0: 'Дракон', 1: "Змея", 2: "Лошадь", 3: "Коза", 4:"Обезьяна", 5:"Петух", 6:"Собака", 7:"Свинья", 8:"Крыса", 9:"Бык", 10:"Тигр", 11:"Кролик"}
print("По китайскому календарю", china[(year+4)%12])