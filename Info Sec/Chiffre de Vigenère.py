# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26       буква -нужная буква -сдвиг
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26

user_str = list(input("Слово для шифровки:").upper())
key_word = list(input("Слово ключ:").upper())
# if str(user_str).upper() in alphabet_EU:
#     print("Yes")
k = 0
index_key_w = []
index_user_w = []

for i in key_word:
    index_key_w.append(alphabet_RU.index(i) + 1)
for i in user_str:
    index_user_w.append(alphabet_RU.index(i) + 1)

new_index = []
for i in

# def Decoding(user_str):
#     new_word = []
#     for i in alphabet_RU:
#         new_word.append(i +)


# print(len(list(alphabet_RU)))
print(index_user_w)

print(index_key_w)


