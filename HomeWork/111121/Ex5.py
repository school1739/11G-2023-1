print("Группы из восьми бит:")
while (bits := input()) != " ":
    if len(bits) == 8 and all(c in ("0", "1") for c in bits):
        print(int(bits.count("1") % 2))
    else:
        print("Error")

# Evaluation: NOT OK. Программа работает наоборот -- выводит бит нечётности.
# Группы из восьми бит:
# 11001100
# 0
# 10000000
# 1