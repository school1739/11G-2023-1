data_packet = input("Введите 8 бит (1 или 0 ): ")
# Делаем проверку на ввод пользователем пустой строки
while data_packet != "" or data_packet != " ":
    # Проверка 8-ми бит на правильность
    if len(data_packet) == 8 and ('1' in data_packet or '0' in data_packet):
        # Проверка на бит четности
        if data_packet.count('1') % 2 == 0:
            print(1)
            data_packet = input("Введите 8 бит (1 или 0 ): ")
        else:
            print(0)
            data_packet = input("Введите 8 бит (1 или 0 ): ")
    else:
        print("Введи 8 бит!")
        break