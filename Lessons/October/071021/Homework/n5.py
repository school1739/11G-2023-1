print("please, enter the number of bottles with a volume less than 1 liter")
bottles_less_than_liter = int(input())
print("and number of bottles with a volume more than 1 liter...")
bottles_more_than_liter = int(input())
cash_for_one_bottle_less_than_liter = 0.10
cash_for_one_bottle_more_than_liter = 0.25
cash_for_all_bottles = bottles_less_than_liter * cash_for_one_bottle_less_than_liter + \
                       cash_for_one_bottle_more_than_liter * bottles_more_than_liter
print("%.2f" % cash_for_all_bottles + '₽')