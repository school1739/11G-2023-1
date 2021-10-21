from datetime import datetime, timedelta

year = int(input("Введите год:" + " "))
month = int(input("Введите месяц:"+ ""))
day = int(input("Введите день:" + ""))
data = datetime(year, month, day)
newdate = data + timedelta(days=1)
newdate = newdate.strftime("%Y-%m-%d")
print(newdate)
