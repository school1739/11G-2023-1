# Скорее всего это задание можно было решить проще. Если Вы объясните как, буду благодарен.
birth = [int(i) for i in input("Enter your birthday split '.' (Day.Month.Year):").split(".")]
znak = 0
if (birth[0] >= 22 and birth[0] <= 31 and birth[1] == 12) or (birth[1] == 1 and birth[0] >= 1 and birth[0] <= 20):
    znak = "Capricorn"
elif (birth[0] >= 21 and birth[0] <= 31 and birth[1] == 1) or (birth[1] == 2 and birth[0] >= 1 and birth[0] <= 18):
    znak = "Aquarius"
elif (birth[0] >= 19 and birth[0] <= 29 and birth[1] == 2) or (birth[1] == 3 and birth[0] >= 1 and birth[0] <= 20):
    znak = "Fishes"
elif (birth[0] >= 21 and birth[0] <= 31 and birth[1] == 3) or (birth[1] == 4 and birth[0] >= 1 and birth[0] <= 19):
    znak = "Aries"
elif (birth[0] >= 20 and birth[0] <= 30 and birth[1] == 4) or (birth[1] == 5 and birth[0] >= 1 and birth[0] <= 20):
    znak = "Taurus"
elif (birth[0] >= 21 and birth[0] <= 31 and birth[1] == 5) or (birth[1] == 6 and birth[0] >= 1 and birth[0] <= 21):
    znak = "Twins"
elif (birth[0] >= 22 and birth[0] <= 30 and birth[1] == 6) or (birth[1] == 7 and birth[0] >= 1 and birth[0] <= 22):
    znak = "Cancer"
elif (birth[0] >= 23 and birth[0] <= 31 and birth[1] == 7) or (birth[1] == 8 and birth[0] >= 1 and birth[0] <= 22):
    znak = "Lion"
elif (birth[0] >= 23 and birth[0] <= 31 and birth[1] == 8) or (birth[1] == 9 and birth[0] >= 1 and birth[0] <= 22):
    znak = "Virgo"
elif (birth[0] >= 23 and birth[0] <= 30 and birth[1] == 9) or (birth[1] == 10 and birth[0] >= 1 and birth[0] <= 23):
    znak = "Scales"
elif (birth[0] >= 24 and birth[0] <= 31 and birth[1] == 10) or (birth[1] == 11 and birth[0] >= 1 and birth[0] <= 22):
    znak = "Scorpion"
elif (birth[0] >= 23 and birth[0] <= 30 and birth[1] == 11) or (birth[1] == 12 and birth[0] >= 1 and birth[0] <= 21):
    znak = "Sagittarius"

dragon = ["Dragon"]
snake = ["Snake"]
horse = ["Horse"]
goat = ["Goat"]
monkey = ["Monkey"]
cock = ["Cock"]
dog = ["Dog"]
pig = ["Pig"]
rat = ["Rat"]
bull = ["Bull"]
tiger = ["Tiger"]
rabbit = ["Rabbit"]
_list = [dragon, snake, horse, goat, monkey, cock, dog, pig, rat, bull, tiger, rabbit]
for i in range(2000, 0, -12):
    dragon.append(i)
for i in range(2001, 0, -12):
    snake.append(i)
for i in range(2002, 0, -12):
    horse.append(i)
for i in range(2003, 0, -12):
    goat.append(i)
for i in range(2004, 0, -12):
    monkey.append(i)
for i in range(2005, 0, -12):
    cock.append(i)
for i in range(2006, 0, -12):
    dog.append(i)
for i in range(2007, 0, -12):
    pig.append(i)
for i in range(2008, 0, -12):
    rat.append(i)
for i in range(2009, 0, -12):
    bull.append(i)
for i in range(2011, 0, -12):
    rabbit.append(i)
for i in range(2010, 0, -12):
    tiger.append(i)
for b in range(0, len(_list)):
    if birth[2] in _list[b]:
        print(f"Your zodiac sign is {znak} "
              f"\nYou are {_list[b][0]} according to chinese calendar")
        break