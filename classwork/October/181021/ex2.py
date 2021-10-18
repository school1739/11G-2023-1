human_age = int(input("введите человеский возраст"))
if human_age >= 0:
    if human_age <= 2:
        dog_age = human_age * 10.5
        print(round(dog_age), "years")
    else:
        dog_age = 2 * 10.5 + (human_age - 2) * 4
        print(round(dog_age), "years")
else:
    print("invalid number")
