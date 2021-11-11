print("Вводи целые числа!")
n = int(input())
sum = 0
end = 0
while n != "":
    sum = sum + int(n)
    n = input()
if sum <= 2.50:
    print("Итогавая сумма:", sum)
    print("Вы заплатите: 0")
else:
    end = sum - (sum%5)
    print("Итогавая сумма:", sum)
    print("Вы заплатите:", end)
