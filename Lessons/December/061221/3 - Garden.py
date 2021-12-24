# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set= set(meadow)

all_the_flowers = garden_set | meadow_set

# выведите на консоль все виды цветов
#print(all_the_flowers)
#for flower in all_the_flowers:
    #print(flower,end=" ")

# выведите на консоль те, которые растут и там и там
#itamitam=garden_set & meadow_set
#for flower in itamitam:
    #print(flower,end=" ")

# выведите на консоль те, которые растут в саду, но не растут на лугу
#rastutnalugu = meadow_set - garden_set
#for flower in rastutnalugu:
    #print(flower,end=" ")

# выведите на консоль те, которые растут на лугу, но не растут в саду
rastutvsadu = garden_set - meadow_set
for flower in rastutvsadu:
    print(flower,end=" ")

# Evaluation: NOT OK. Почему только один вывод?