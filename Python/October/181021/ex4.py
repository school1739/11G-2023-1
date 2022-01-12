a = int(input('Количество сторон: '))
if a < 3 or a > 10:
    print('Введите число в диапозоне от 3 до 10 включительно')
    exit(-1)

if a == 3:
    s = 'тре'
elif a == 4:
    s = 'четырёх'
elif a == 5:
    s = 'пяти'
elif a == 6:
    s = 'шести'
elif a == 7:
    s = 'семи'
elif a == 8:
    s = 'восьми'
elif a == 9:
    s = 'девяти'
elif a == 10:
    s = 'десяти'


print(f'Это {s}угольник')

# Evaluation: OK