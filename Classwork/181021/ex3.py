a = input().lower()

if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('Гласная')
elif a == 'y':
    print('Может быть и гласной и согласной')
else:
    print('Согласная')
