year = int(input("Введите год: "))
month = input("Введите месяц (в родительном падаже!): ")
day = int(input("Введите день: "))
if day == 31:
    if month == "января":
        print("1 февраля", year, "года")
    elif month == "марта":
        print("1 апреля", year, "года")
    elif month == "мая":
        print("1 июня", year, "года")
    elif month == "июля":
        print("1 августа", year, "года")
    elif month == "августа":
        print("1 сентября", year, "года")
    elif month == "октября":
        print("1 ноября", year, "года")
    elif month == "декабря":
        print("1 января", year+1, "года")
    else:
        print("Такого дня месаца нет :(")
elif day == 30:
    if month == "апреля":
        print("1 мая", year, "года")
    elif month == "июня":
        print("1 июля", year, "года")
    elif month == "сентября":
        print("1 октября", year, "года")
    elif month == "ноября":
        print("1 декабря", year, "года")
    else:
        print("Такого дня месаца нет :(")
elif day == 28 and month == "февраля":
    if year % 4 == 0:
        print("29 февраля", year, "года")
    else:
        print("1 марта", year, "года")
elif day == 29 and month == "февраля":
    if year % 4 == 0:
        print("1 марта", year, "года")
    else:
        print("Такого дня месаца в этом году нет :(")
elif day > 31:
    print("Такого дня месаца нет :(")

else:
    print(day + 1, month, year, "года")