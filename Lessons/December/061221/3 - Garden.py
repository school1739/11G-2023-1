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
all_flowers = garden_set | meadow_set #Или там или там
print("Все цветы: ", end="")
for flower in all_flowers:
    print(flower, end=" ")
print()
# выведите на консоль те, которые растут и там и там
itamitam = garden_set & meadow_set #И там и там
print("И там, и там: ", end="")
for flower in itamitam:
    print(flower, end=" ")
print()

# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_and_not_meadow = garden_set - meadow_set #Вычетание
print("В саду, но не на лугу: ", end="")
for flower in garden_and_not_meadow:
    print(flower, end=" ")
print()

# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_and_not_garden = meadow_set - garden_set #Вычетание
print("В лугу, но не в саду: ", end="")
for flower in meadow_and_not_garden:
    print(flower, end=" ")
print()

# Evaluation: OK. Да не работаем мы в папке Lessons, ну!