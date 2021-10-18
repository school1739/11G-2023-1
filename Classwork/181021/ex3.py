let=str(input("Буква латинского алфавита: "))
if let == "a" or let=="o" or let=="i" or let=="e" or let == "u":
    print('Гласная')
elif let=="y":
    print('Гласная и согласная')
else:
    print('Согласная')