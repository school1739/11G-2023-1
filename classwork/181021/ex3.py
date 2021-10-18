let=str(input('буква латинского алфавита'))
if let == "a" or let == "e" or let == "i" or let == "u" or let == "o":
    print('гласная')
elif let == "y":
    print("и согласная и гласная")
else:
    print("это буква согласная")