print("Введите группы из восьми бит (завершите ввод пустой строкой)")

entering = True
while entering:
    s = input()
    if s == "":
        entering = False
    elif len(s) == 8:
        total = 0

        is_correct = True
        i = 0
        while is_correct and i < 8:
            if s[i].isnumeric():
                x = int(s[i])
                if x == 0 or x == 1:
                    total += x
                    i += 1
                else:
                    is_correct = False
            else:
                is_correct = False

        if is_correct:
            parity_bit = 0
            if total % 2 == 0:
                parity_bit = 0
            else:
                parity_bit = 1
            print("Бит чётности:", parity_bit)
        else:
            print("Введён некорректный символ в последовательности (не 0 или 1)!")
    else:
        print("Введена последовательность длиной не в 8 бит!")

# Evaluation: NOT OK. Программа работает наоборот -- выводится бит НЕЧЁТНОСТИ.
# Введите группы из восьми бит (завершите ввод пустой строкой)
# 11001100
# Бит чётности: 0
# 10000000
# Бит чётности: 1