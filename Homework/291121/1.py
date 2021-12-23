# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

for k in sites.keys():
    site = sites[k]
    x1 = site[0]
    y1 = site[1]
    distances[k] = {}
    k_keys = list(sites.keys())
    k_keys.remove(k)
    for n in k_keys:
        nsite = sites[n]
        x2 = nsite[0]
        y2 = nsite[1]
        distances[k][n] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

for k in distances.keys():
    for n in distances[k].keys():
        print("%s - %s: %.2f" %(k, n, distances[k][n]))

# Evaluation: +-OK. По заданию надо было создать словарь словарей.