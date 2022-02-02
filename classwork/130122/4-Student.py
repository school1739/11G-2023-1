# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Январь: # для каждого месяца!
#       Расходы: ХХХ.ХХ рублей.
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = int(input("Стипендия - ")), int(input("Расходы - "))


months = ['September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June']


for month in months:
    if month == 'September':
        cash_by_parents = expenses - educational_grant
        print("September:")
        print("Расходы:", expenses, "рублей")
        print("Студенту надо попросить", cash_by_parents, "рублей")
        print()
    else:
        cash_by_parents = round(expenses) - educational_grant
        print(month + ":")
        print("Расходы:", round(expenses), "рублей")
        print("Студенту надо попросить", cash_by_parents, "рублей")
        print()
    expenses *= 1.03

# OK