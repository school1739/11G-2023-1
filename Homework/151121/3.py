from random import choice

total_simulations = 10
total_tries = 0
for k in range(total_simulations):
    tries = 0
    repeats = 0
    prev = ""
    while repeats < 3:
        current = choice(['О', 'Р'])
        if repeats == 0 or current != prev:
            prev = current
            repeats = 1
        else:
            repeats += 1
        tries += 1
        print(current, end=" ")
    total_tries += tries
    print("(попыток: %d)" % tries)

avg = total_tries / total_simulations
print("Среднее количество попыток: %.1f" % avg)

# Evaluation: OK