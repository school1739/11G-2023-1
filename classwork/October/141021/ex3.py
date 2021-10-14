suvenir = int(input("введите количество сувениров, которые вы купили"))
bezdelushka = int(input("введите количество безделушек, которые вы купили"))
weight_of_suvenir = suvenir * 75
weight_of_bezdelushka = bezdelushka * 112
total_weight = (weight_of_suvenir + weight_of_bezdelushka) / 1000
print("%.2f" % total_weight, "кг")