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

# список тестовых значений размеров бумаги (X, Y)
paper_tests = [
    (8, 9),
    (9, 8),
    (6, 8),
    (8, 6),
    (3, 4),
    (11, 9),
    (9, 11)
]

# размеры конверта
envelop_x = int(input('Введите длину конверта: '))
envelop_y = int(input('Введите ширину конверта: '))

# для каждого листа бумаги из списка
for paper in paper_tests:
    paper_x = paper[0]
    paper_y = paper[1]
    # проверяем, помещается ли в конверт
    if (paper_x <= envelop_x and paper_y <= envelop_y) or (
            paper_x <= envelop_y and paper_y <= envelop_x):
        print("ДА")
    else:
        print("НЕТ")

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

# список тестовых значений размеров кирпичей (X, Y, Z)
brick_tests = [
    (11, 10, 2),
    (11, 2, 10),
    (10, 11, 2),
    (10, 2, 11),
    (2, 10, 11),
    (2, 11, 10),
    (3, 5, 6),
    (3, 6, 5),
    (6, 3, 5),
    (6, 5, 3),
    (5, 6, 3),
    (5, 3, 6),
    (11, 3, 6),
    (11, 6, 3),
    (6, 11, 3),
    (6, 3, 11),
    (3, 6, 11),
    (3, 11, 6)
]

# размеры отверстия
hole_x = int(input('Введите длину отверстия: '))
hole_y = int(input('Введите ширину отверстия: '))

# для каждого кирпича из списка
for brick in brick_tests:
    brick_x = brick[0]
    brick_y = brick[1]
    brick_z = brick[2]

    # проверяем, проходит ли хотя бы одна из трёх уникальных граней в отверстие
    if brick_x <= hole_x and brick_y <= hole_y or \
            brick_x <= hole_x and brick_z <= hole_y or \
            brick_y <= hole_x and brick_x <= hole_y or \
            brick_y <= hole_x and brick_z <= hole_y or \
            brick_z <= hole_x and brick_x <= hole_y or \
            brick_z <= hole_x and brick_y <= hole_y:
        print("ДА")
    else:
        print("НЕТ")
