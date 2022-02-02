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

envelop_x = int(input("Enter the width of the envelope:"))
envelop_y = int(input("Enter the height of the envelope:"))
paper = [(8, 9), (9, 8), (6, 8), (8, 6), (3, 4), (11, 9), (9, 11)]
# Проверка значений
for i in paper:
    if i[0] <= envelop_x and i[1] <= envelop_y:
        print('Yes')
    elif i[0] <= envelop_y and i[1] <= envelop_x:
        print('Yes')
    else:
        print('No')

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

hole_x, hole_y = int(input("Enter the width of the hole:")), int(input("Enter the len of the hole:"))

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
    # Проверка значений
    if size[0] <= hole_x and size[1] <= hole_y:
        print("YES")
    elif size[1] <= hole_x and size[0] <= hole_y:
        print("YES")
    elif size[0] <= hole_x and size[2] <= hole_y:
        print("YES")
    elif size[2] <= hole_x and size[0] <= hole_y:
        print("YES")
    elif size[2] <= hole_x and size[1] <= hole_y:
        print("YES")
    elif size[1] <= hole_x and size[2] <= hole_y:
        print("YES")
    else:
        print("NO")

# OK