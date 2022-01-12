from datetime import datetime, timedelta

year = int(input('Год: '))
month = int(input('Месяц: '))
day = int(input('День: '))

date = datetime(year, month, day)
next_date = date + timedelta(days=1)

print(f'Следующий день: {next_date.strftime("%d.%m.%Y")}')

# Evaluation: OK