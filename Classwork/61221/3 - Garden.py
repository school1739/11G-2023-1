# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
all_the_flowers=garden_set|meadow_set
print(' '.join([i for i in all_the_flowers]))
# выведите на консоль те, которые растут и там и там
itamitam = garden_set & meadow_set
print(' '.join([i for i in itamitam]))

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_meadow =garden_set-meadow_set
print(' '.join(garden_meadow))

# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_garden = meadow_set-garden_set
print(' '.join(meadow_garden))