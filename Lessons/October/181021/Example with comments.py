# Ввод координат от пользователя
pointX = int(input("Введите X: "))
pointY = int(input("Введите Y: "))

# Начало условного перехода
if pointX > 0 and pointY > 0:  # Проверка на 1 четверть
    print("1 четверть")  # Вывод ответа, если удовлетворяет условию
elif pointX < 0 and pointY > 0:
    print("2 четверть")
elif pointX < 0 and pointY < 0:
    print("3 четверть")
else:  # ВСЕ ОСТАЛЬНЫЕ СЛУЧАИ
    print("4 четверть")
