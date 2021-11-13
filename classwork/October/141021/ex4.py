deposit = int(input("введите сумму первоначального депозита"))
money_after_one_year = deposit + deposit * 0.04
money_after_two_years = money_after_one_year + money_after_one_year * 0.04
money_after_three_years = money_after_two_years + money_after_two_years * 0.04
print("сумма денег после одногодового вклада:", "%.2f" % money_after_one_year, "₽")
print("сумма денег после двухгодового вклада:", "%.2f" % money_after_two_years, "₽")
print("сумма денег после трехгодового вклада:", "%.2f" % money_after_three_years, "₽")

# Evaluation: OK