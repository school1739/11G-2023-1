from pprint import pprint
from math import hypot

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
for (city_from, (x1, y1)) in sites.items():
    # Словарь с расстояниями от текущего города
    current_distances = {}

    for (city_to, (x2, y2)) in sites.items():
        # Исключаем расстояния между одним и тем же городом
        if city_from != city_to:
            # Вычисляем расстояние
            current_distances[city_to] = hypot(x1 - x2, y1 - y2)
    # Добавляем расстояния в общий словарь
    distances[city_from] = current_distances

# Выводим все города
pprint(distances)
