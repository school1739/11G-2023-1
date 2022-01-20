# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

# АВТОМАТИЧЕСКИ проверить для:
# paper_x, paper_y = 8, 9
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (написать цикл для проверки)

envelop_size = (int(input('Ширина конверта: ')), int(input('Длина конверта: ')))
paper_sizes = [
    (8, 9), (9, 8), (6, 8),
    (8, 6), (3, 4), (11, 9),
    (9, 11)
]

for paper_size in paper_sizes:
    if paper_size[0] <= envelop_size[0] and paper_size[1] <= envelop_size[1]:
        print('Да')
    else:
        print('Нет')



# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# АВТОМАТИЧЕСКИ проверить для:
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (написать цикл для проверки)

hole_x_y = int(input("Введите ширину отверстия:")),int(input("Введите длину отверстия:"))


size_brick = [
    [11, 10, 2],
    [11, 2, 10],
    [10, 11, 2],
    [10, 2, 11],
    [2, 10, 11],
    [2, 11, 10],
    [3, 5, 6],
    [3, 6, 5],
    [6, 3, 5],
    [6, 5, 3],
    [5, 6, 3],
    [5, 3, 6],
    [11, 3, 6],
    [11, 6, 3],
    [6, 11, 3],
    [6, 3, 11],
    [3, 6, 11],
    [3, 11, 6],
]
for size in size_brick:
    size.remove(max(size))
    if size[0]<=hole_x_y[0] and size[1]<=hole_x_y[0]:
        print("Да")
    elif size[1]<=hole_x_y[0] and size[0]<=hole_x_y[0]:
        print("Да")
    else:
        print("Нет")

