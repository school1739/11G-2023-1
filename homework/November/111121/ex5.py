print("Введите группы из восьми бит:")
while (bits := input()) != " ":
    if len(bits) == 8 and all(c in ("0", "1") for c in bits):
        print(int(bits.count("1") % 2))
    else:
        print("Error")