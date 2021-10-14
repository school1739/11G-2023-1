a = int(input('Сумма первоначального депозита: '))

for i in range(1, 4):
    a *= 1.04
    print(f'{i}-й год: {a:.2f}')
