s = float(input())
a = s * 0.18

print(f'Чаевые: {a:.2f}\n'
      f'Налог: {a:.2f}\n'
      f'Итог: {s - 2*a:.2f}')
