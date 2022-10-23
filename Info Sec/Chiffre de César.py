alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = int(input('Какой шаг шифровки: '))
text = input("Сообщение для дешифровки: ").upper()
result = ''
lang = input('Выберите язык русский(1)/английский(2): ')
if lang == '1':
    for i in text:
        position = alfavit_RU.find(i)
        position_1 = position + step
        if i in alfavit_RU:
            result += alfavit_RU[position_1]
        else:
            result += i
else:
    for i in text:
        position = alfavit_EU.find(i)
        position_1 = position + step
        if i in alfavit_EU:
            result += alfavit_EU[position_1]
        else:
            result += i
print (result)