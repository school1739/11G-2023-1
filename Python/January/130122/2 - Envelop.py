# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

# АВТОМАТИЧЕСКИ проверить для:
# ввод размера
evelop_x=int(input("введите ширину листа"))
evelop_y=int(input("введите длину листа"))
# Размеры листов
size_of_paper =[
    [8,9],
    [9,8],
    [6,8],
    [8,6],
    [3,4],
    [11,9],
    [9,11],
]
# paper_x, paper_y = 8, 9
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# цикл для проверки
for papers in size_of_paper:
    if envelop_x <= papers[0] and envelop_y <= papers[1]:
        print("да")
    elif envelop_y <= papers[0] and envelop_x <= papers[1]:
        print("да")
    else:
        print("нет")

# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)
# ввод размеров отверстий
hole_x = int(input("ширина отверстия"))
hole_y = int(input("длина отверстия"))
#размер кирпича
size_of_brick=[
    [11,10,2],
    [11,2,10],
    [10,11,2],
    [2,10,11],
    [2,11,10],
    [3,5,6],
    [3,6,5],
    [5,3,6],
    [5,6,3],
    [6,3,5],
    [6,5,3],
    [11,3,6],
    [11,6,3],
    [3,11,6],
    [3,6,11],
    [6,11,3],
    [6,3,11],
]

#проверка проходимости
for bricks in size_of_brick:
    if brick[0] < hole_x and bricks[1] <= hole_y:
        print ("да")
    elif bricks[1] <= hole_x and bricks[0] <= hole_y:
        print ("да")
    elif bricks[0] <= hole_x and bircks[2] <= hole_y:
        print ("да")
    elif bricks[2] <= hole_x and bricks[0] <= hole_y:
        print ("да")
    elif bricks[2] <= hole_x and bricks[1] <= hole_y:
        print ("да")
    elif bricks[1] <= hole_x and bricks[2] <= hole_y:
        print ("да")
    else:
        print ("нет")
