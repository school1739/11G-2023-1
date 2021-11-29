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
msk_ldn = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
msk_prs = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5
prs_ldn = ((paris[0] - london[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** 0.5
distances["Moscow"] = {}
distances["Moscow"]["London"] = str(msk_ldn) + "km"
distances["Moscow"]["Paris"] = str(msk_prs) + "km"

distances["London"] = {}
distances["London"]["Moscow"] = str(msk_ldn) + "km"
distances["London"]["Paris"] = str(prs_ldn) + "km"

distances["Paris"] = {}
distances["Paris"]["Moscow"] = str(msk_prs) + "km"
distances["London"]["Paris"] = str(prs_ldn) + "km"
for i in distances:
    print(i, distances[i])

print(distances)
