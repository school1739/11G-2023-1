# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}


# Проходим через все города
for city_from in sites.keys():
    distances[city_from] = {}
    # Находим координаты 1-ого города
    x1, y1 = sites[city_from]
    for city_to in sites.keys():
        # Исключаем расстояние между одним и тем же городом
        if city_from != city_to:
            # Координаты 2-ого города
            x2, y2 = sites[city_to]
            # Вычисляем расстояние
            distances[city_from][city_to] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(distances)
