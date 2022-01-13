import math

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

moscow = sites["Moscow"]
london = sites["London"]
paris = sites["Paris"]

# расчет расстояние между городами
moscow_to_London = math.sqrt(((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2))
london_to_paris = math.sqrt(((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2))
paris_to_moscow = math.sqrt(((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2))

# добавления словарей в словарь
distances["Moscow"] = {}
distances["Moscow"]["London"] = str(moscow_to_London) + " km"
distances["Moscow"]["Paris"] = str(paris_to_moscow) + " km"

distances["Paris"] = {}
distances["Paris"]["Moscow"] = str(paris_to_moscow) + " km"
distances["Paris"]["London"] = str(london_to_paris) + " km"

distances["London"] = {}
distances["London"]["Moscow"] = str(moscow_to_London) + " km"
distances["London"]["Paris"] = str(london_to_paris) + " km"

# функция вывода словаря
for i in distances:
    print(i, distances[i])