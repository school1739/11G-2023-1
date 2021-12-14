import random

# ввод пользователем количества симуляций и количество выполняемых одинаковых событий
number_of_simulations = int(input("enter the number of simulations - "))
goal = int(input("And the number identical events... "))

all_attempt = 0
event_with_heads = 0
event_with_tails = 0

# повторяем симуляцию
for i in range(number_of_simulations):
    attempt = 0
    the_side_of_the_coin = random.randint(0, 1)
    event_with_heads = 0
    event_with_tails = 0

    # выполняем симуляцию
    while event_with_tails != goal and event_with_heads != goal:
        the_side_of_the_coin = random.randint(0, 1)
        # определяем сторону подбросившейся монетки
        if the_side_of_the_coin == 1:
            event_with_tails += 1
            event_with_heads = 0
            print("Р", end="\t")
        else:
            event_with_heads += 1
            event_with_tails = 0
            print("О", end="\t")
        attempt += 1

    all_attempt += attempt
    print("(Попыток: {:d})".format(attempt))

print("average number of flip:", all_attempt / number_of_simulations,
      "flip(s)\nP.S: if u want the integer number, that average number of flip:",
      all_attempt // number_of_simulations, "flip(s)")

# Evaluation: OK