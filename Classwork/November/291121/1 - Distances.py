# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
Moscow = sites("Moscow")
London = sites("London")
Paris = sites("Paris")

msk_ldn = ((Moscow[0] - London[0]) ** 2 + (Moscow[1] - London[1]) ** 2) ** 0.5
msk_prs = ((Moscow[0] - Paris[0]) ** 2 + (Moscow[1] - Paris[1]) ** 2) ** 0.5
prs_ldn = ((Paris[0] - London[0]) ** 2 + (Paris[1] - London[1]) ** 2) ** 0.5

distances = {}

distances["Moscow"] = {}
distances["Moscow"]["London"] = str(msk_ldn) + "km"
distances["Moscow"]["Paris"] = str(msk_prs) + "km"

distances["Moscow"] = {}
distances["London"]["Moscow"] = str(msk_ldn) + "km"
distances["London"]["Paris"] = str(prs_ldn) + "km"

distances["Moscow"] = {}
distances["Paris"]["Moscow"] = str(msk_ldn) + "km"
distances["Paris"]["London"] = str(prs_ldn) + "km"
print(distances)

# Evaluation: NOT OK
# File "/Classwork/November/291121/1 - Distances.py", line 13, in <module>
#     Moscow = sites("Moscow")
# TypeError: 'dict' object is not callable