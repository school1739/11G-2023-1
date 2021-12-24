bin_num = int(input("Введите двоичное число: "))
sum = ''
sum2 = ''
# Номер цифры с строке
index = 0
# Вывод метода расстановки степеней
for i in range(len(str(bin_num)) - 1, -1, -1):
    sum += f"{list(str(bin_num))[index]}∙2^{str(i)} + "
    sum2 += f"{int(list(str(bin_num))[index]) * (2 ** i)} + "
    index += 1
print(f"{bin_num}(2) = {sum[0:-2]}= {sum2[0:-2]}= {int(str(bin_num), 2)}(10)"
      f"\n"
      f"\nОтвет: "
      f"\n{bin_num}(2) = {int(str(bin_num), 2)}(10)")

# Evaluation: OK