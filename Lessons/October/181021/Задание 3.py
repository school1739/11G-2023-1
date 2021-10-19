n = input("Введите букву латинского алфавита: ")
if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
    print("Гласная")
elif n == 'y':
    print("Как гласная, так и согласная")
else:
    print("Согласная")