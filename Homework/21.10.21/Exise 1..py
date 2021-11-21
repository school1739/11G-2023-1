from datetime import datetime, timedelta# разница между 2 моментами времени

year = int(input('Год: '))
month = int(input('Месяц: '))
day = int(input('День: '))

date = datetime(year, month, day)# данная дата
next_date = date + timedelta(days=1)# рассчет след.дня

print(f'Следующий день: {next_date.strftime("%d.%m.%Y")}')# итог

