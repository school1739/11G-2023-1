data_packet = input("Введите 8 бит (1 или 0 ): ")
while data_packet!="" or data_packet!= " ":
    if len(data_packet)==8:
        if data_packet.count('1')%2==0:
            print(1)
            data_packet = input("Введите 8 бит (1 или 0 ): ")
        else:
            print(0)
            data_packet = input("Введите 8 бит (1 или 0 ): ")
    else:
        print("Введи 8 бит!Дурак")
        break