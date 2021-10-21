import datetime

# введение даты
day = int(input("введите день:"))
month = int(input("введите месяц"))
year = int(input("введите год"))

# определение следующего дня
date = datetime.datetime(year, month, day)
next_date = date + datetime.timedelta(days=1)

# вывод следующей даты
print(f'Следующий день после вашего введенного: {next_date.strftime("%d.%m.%Y")}')


