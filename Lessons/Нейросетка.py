sticks = 10
player_turn = 1
while sticks >0:
    print(f'Сколько палок берешь? осталось палок-{sticks}')
    taken = int(input())
    if taken <1 or taken >3:
        print("Надо взять 1 или 3")
        continue
    sticks -= taken
    print(f'было взято {taken}\n')

    if sticks <= 0:
        print(f'Палок больше не осталось. \nPlayer{player_turn} проиграл')
    player_turn = 1 if player_turn ==2 else 2
#я не понял как должна нейронка выглядеть, но вот палочки на двух человек:)


