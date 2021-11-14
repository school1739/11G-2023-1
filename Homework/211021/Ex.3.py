# вводим данные для базового тарифа
number_of_minutes_in_basic_tariff = 50
number_of_sms_in_basic_tariff = 50
payment_for_basic_tariff = 15.00

# вводим данные для дполнительного тарифа
payment_for_minutes_in_extra_tariff = 0.25
payment_for_sms_in_extra_tariff = 0.15
payment_for_support_911 = 0.44

# ввод пользователем данных о его тарифных расходах за месяц
number_of_spent_minutes = int(input("pls, enter the number of spent minutes"))
number_of_spent_sms = int(input("and the number of spent sms"))

# расчет платы за дополнительные минуты и смc, также налога и итоговой суммы
payment_for_extra_minutes = (number_of_spent_minutes - number_of_minutes_in_basic_tariff) * payment_for_minutes_in_extra_tariff
payment_for_extra_sms = (number_of_spent_sms - number_of_sms_in_basic_tariff) * payment_for_sms_in_extra_tariff
tax = (payment_for_basic_tariff + payment_for_support_911 + payment_for_extra_minutes + payment_for_extra_sms) * 0.05
total_payment = tax + payment_for_support_911 + payment_for_basic_tariff + payment_for_extra_minutes + payment_for_extra_sms


if number_of_spent_minutes <= number_of_minutes_in_basic_tariff and number_of_spent_sms <= number_of_sms_in_basic_tariff:

    tax = (payment_for_basic_tariff + payment_for_support_911) * 0.05
    total_payment = tax + payment_for_support_911 + payment_for_basic_tariff

    print("basic tariff -", payment_for_basic_tariff, "$")
    print("payment for support 911 -", payment_for_support_911, "$")
    print("tax -", "%.2f" % tax, "$")
    print("total payment -", "%.2f" % total_payment, "$")


elif number_of_spent_minutes > number_of_minutes_in_basic_tariff and number_of_spent_sms <= number_of_sms_in_basic_tariff:

    tax = (payment_for_basic_tariff + payment_for_support_911 + payment_for_extra_minutes) * 0.05
    total_payment = tax + payment_for_support_911 + payment_for_basic_tariff + payment_for_extra_minutes

    print("basic tariff -", payment_for_basic_tariff, "$")
    print("payment for support 911 -", payment_for_support_911, "$")
    print("tax -", "%.2f" % tax, "$")
    print("payment for extra minutes -", "%.2f" % payment_for_extra_minutes, "$")
    print("total payment -", "%.2f" % total_payment, "$")


elif number_of_spent_minutes <= number_of_minutes_in_basic_tariff and number_of_spent_sms > number_of_sms_in_basic_tariff:

    tax = (payment_for_basic_tariff + payment_for_support_911 + payment_for_extra_sms) * 0.05
    total_payment = tax + payment_for_support_911 + payment_for_basic_tariff + payment_for_extra_sms

    print("basic tariff -", payment_for_basic_tariff, "$")
    print("payment for support 911 -", payment_for_support_911, "$")
    print("tax -", "%.2f" % tax, "$")
    print("payment for extra sms -", "%.2f" % payment_for_extra_sms, "$")
    print("total payment -", "%.2f" % total_payment, "$")


else:

    tax = (payment_for_basic_tariff + payment_for_support_911 + payment_for_extra_minutes + payment_for_extra_sms) * 0.05
    total_payment = tax + payment_for_support_911 + payment_for_basic_tariff + payment_for_extra_minutes + payment_for_extra_sms

    print("basic tariff -", payment_for_basic_tariff, "$")
    print("payment for support 911 -", payment_for_support_911, "$")
    print("tax -", "%.2f" % tax, "$")
    print("payment for extra minutes -", "%.2f" % payment_for_extra_minutes, "$")
    print("payment for extra sms -", "%.2f" % payment_for_extra_sms, "$")
    print("total payment -", "%.2f" % total_payment, "$")

# Evaluation: OK. Скопипастил у Карныгина, и даже рефакторинг названий переменных не сделал. Фу таким быть.