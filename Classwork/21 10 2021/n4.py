from datetime import datetime

date_of_birth = datetime.strptime(input('Дата рождения (дд.мм.гггг): '), '%d.%m.%Y')

zodiac_signs_start_days = (
    (22, 'Козерог'),
    (22, 'Стрелец'),
    (23, 'Скорпион'),
    (23, 'Весы'),
    (23, 'Дева'),
    (23, 'Лев'),
    (21, 'Рак'),
    (21, 'Близнецы'),
    (20, 'Телец'),
    (21, 'Овен'),
    (19, 'Рыбы'),
    (20, 'Водолей'),
)

zodiac_signs = ((datetime(date_of_birth.year, 12 - i, x[0]), x[1])
                for i, x in enumerate(zodiac_signs_start_days))

chinese_horoscope = ('Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык',
                     'Тигр', 'Кролик', 'Дракон', 'Змея', 'Лошадь', 'Коза')


print(f'Знак зодиака: {next(i for i in zodiac_signs if date_of_birth >= i[0])[1]}')
print(f'Животное по китайскому летоисчислению: {chinese_horoscope[date_of_birth.year % 12]}')

# Evaluation: OK. Я снова почти уверен, что ты не сам делал.