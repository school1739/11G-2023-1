# Просим ввести 8 бит
data_packet = input(("Введите 8 бит"))
#  Проверяем и выдаём чётность или нечётность 1
while data_packet != "" or data_packet != " ":
    if data_packet.count ("1") %2 == 0:
        print(1)
        data_packet = input(("Введите 8 бит"))
    else:
        print (0)
        data_packet = input(("Введите 8 бит"))
        break

# Evaluation: OK