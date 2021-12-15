# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

garden_set = set(garden)
meadow_set = set(meadow)
all_the_flowers = garden_set | meadow_set


# выведите на консоль все виды цветов
for flower in all_the_flowers:
    print(flower, end=" ")


# выведите на консоль те, которые растут и там и там
ii = garden_set & meadow_set
print("И там, и там: ", end="")
for flower in ii:
    print(flower, end=" ")
print()

# выведите на консоль те, которые растут в саду, но не растут на лугу
vsadu = garden_set - meadow_set
for flower in vsadu:
    print(flower, end=" ")
# выведите на консоль те, которые растут на лугу, но не растут в саду
nalugu = meadow_set - garden_set
for flower in nalugu:
    print(flower, end=" ")