print("Введите название месяца")
month = input()
if month == "январь" and "март" and "май" and "май" and "июль" and "август" and "октябрь" and "декабрь":
    print(31, "день")
elif month == "апрель" and "июнь" and "сентябрь" and "ноябрь":
    print(30, "день")
elif month == "февраль":
    print(28, "день")
else:
    print("Введите коректное название")