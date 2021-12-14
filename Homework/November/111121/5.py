print('Введите группы из восьми бит:')
while (bits := input()) != '':                                    # Вводим биты пока не будет пустая строка
    if len(bits) == 8 and all(c in ('0', '1') for c in bits):     # Выводим бит чётности
        parity_bit = bits.count('1') % 2
        print(parity_bit)
    else:                                                         # Неверный ввод
        print('Error')

# Evaluation: NOT OK
# >10011001
# >0
# >11111111
# >0
# >11111100
# >0
# >1
# >Error
# >11000000
# >0