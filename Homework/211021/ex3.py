basic_minutes = 50
basic_messages = 50
tariff_plan_cost = 15
extra_minute_cost = 0.25
extra_message_cost = 0.15
call_center_tax = 0.44
tax_percentage = 0.05

total_minutes = int(input('Количество израсходованных минут разговора: '))
total_messages = int(input('Количество израсходованных смс-сообщений: '))

extra_minutes_cost = (total_minutes - basic_minutes) * extra_minute_cost
extra_messages_cost = (total_messages - basic_messages) * extra_message_cost
cost_without_tax = tariff_plan_cost + extra_minutes_cost + extra_messages_cost + call_center_tax
tax = cost_without_tax * tax_percentage
total_cost = cost_without_tax + tax


print(f'Базовая сумма тарификации: {tariff_plan_cost}$')
if total_minutes > basic_minutes:
    print(f'Сумма за дополнительные минуты: {extra_minutes_cost}$')
if total_messages > basic_messages:
    print(f'Сумма за дополнительные сообщения: {extra_messages_cost}$')
print(f'Сумма отчислений кол-центрам 911: {call_center_tax}$')
print(f'Налог: {tax:.2f}$')
print(f'Итоговая сумма к оплате: {total_cost:.2f}$')
