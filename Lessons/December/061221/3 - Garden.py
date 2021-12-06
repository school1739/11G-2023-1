# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

#all_the_flowers= garden_set|meadow_set
#print(all_the_flowers)
#for flowers in all_the_flowers:
    #print(flowers,and=" ")
# выведите на консоль все виды цветов
#all_the_flowers= garden_set|meadow_set
#print(all_the_flowers)
#for flowers in all_the_flowers:
    #print(flowers,and=" ")

# выведите на консоль те, которые растут и там и там
#itamitam=garden_set & meadow_set
#for flowers in itamitam:
    #print(itamitam)

# выведите на консоль те, которые растут в саду, но не растут на лугу
#vsadu=garden_set - meadow_set
#for flowers in vsadu:
   #print(flowers, end=" ")

# выведите на консоль те, которые растут на лугу, но не растут в саду
#nalugu=meadow_set - garden_set
#for flowers in nalugu:
    #print(flowers, end=" ")
