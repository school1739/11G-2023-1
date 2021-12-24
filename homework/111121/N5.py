data_of_packet = input("Введиет 8 байтов :")
# определяем корректность введенных данных и четность бит
while data_of_packet != "":
    if len(data_of_packet) == 8:
        if data_of_packet.count("1") % 2 == 0:
            print(1)
            data_of_packet = input("Введиет 8 байтов :")
            break
        else:
            print(0)
            data_of_packet = input("Введите 8 байтов :")
            break
    else:
        print("Кол-во байтов неверно")
        break

# Evaluation: NOT OK. Не работает, когда бит # Введиет 8 байтов :11001100
# # 1
# # Введиет 8 байтов :10000000
# #
# # Process finished with exit code 0нечётный.
