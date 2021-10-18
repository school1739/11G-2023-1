latin_letter = str(input("введите букву латинского алфавита"))
if latin_letter == "a" or latin_letter == "e" or latin_letter == "i" or latin_letter == "o" or latin_letter == "u":
    print("ваша буква гласная")
elif latin_letter == "y":
    print("ваша буква и гласная, и согласная")
else:
    print("ваша буква согласная")
