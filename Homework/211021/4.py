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
_list = ['monkey', 'cock', ' dog', 'pig', 'rat', 'bull', 'tiger', 'rabbit', 'dragon', 'snake', ' horse', 'goat']
print(f"Your zodiac sign is {znak} "
      f"\nYou are {_list[birth[2] % 12]} according to chinese calendar")

# Evaluation: OK. Отличное оформление, btw!