# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ '

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26       -буква -нужная буква -сдвиг?
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26

from itertools import cycle

user_str = list(input("Слово(а) для шифровки/расшифровки(без пробелов!): ").upper())
key_word = list(input("Слово(а) ключ(без пробелов!): ").upper())

if user_str[0] in alphabet_RU:  # Узнаём язык слова
    alphabet = alphabet_RU
    print("Язык - русский")
else:
    alphabet = alphabet_EU
    print("Язык - английский")
# Узнаем индексы букв введенного слова и слова-ключа
index_key_w = []
index_user_w = []
for i in key_word:
    if i != " ":
        index_key_w.append(alphabet.index(i) + 1)
    else:
        index_key_w.append(0)
for i in user_str:
    if i != " ":
        index_user_w.append(alphabet.index(i) + 1)
    else:
        index_user_w.append(0)


def encryption(alphabet):  # Функция для шифровки
    new_index = []
    for old, new in enumerate(cycle(index_key_w)):  # Высчитываем новый индекс для зашифрованной буквы
        if old >= len(user_str):
            break
        new_index.append(index_user_w[old] + new)
    return new_index


encryption_word = ''.join([alphabet[char - 1] for char in encryption(alphabet)])


def brute_forse(encryption_word, alphabet):
    index_encryption_word = []
    for i in encryption_word:  # Узнаем индексы букв зашифрованного слова
        index_encryption_word.append(alphabet.index(i) + 1)

    index_decryption_w = []
    for old, new in enumerate(cycle(index_key_w)):  # Высчитываем индекс для расшифрованной буквы
        if old >= len(encryption_word):
            break
        index_decryption_w.append(index_encryption_word[old] - new)

    return index_decryption_w


i_d_w = brute_forse(user_str, alphabet)
brute_forse_word1 = ''.join([alphabet[char - 1] for char in i_d_w])
i_d_w_rev = list(reversed(i_d_w))
brute_forse_word2 = ''.join([alphabet[char - 1] for char in i_d_w_rev])


def decryption(encryption_word, alphabet):  # Функция для расшифровки
    index_encryption_word = []
    for i in encryption_word:  # Узнаем индексы букв зашифрованного слова
        index_encryption_word.append(alphabet.index(i) + 1)

    index_decryption_w = []
    for old, new in enumerate(cycle(index_key_w)):  # Высчитываем индекс для расшифрованной буквы
        if old >= len(encryption_word):
            break
        index_decryption_w.append(index_encryption_word[old] - new)

    return index_decryption_w


decryption_word = ''.join([alphabet[char - 1] for char in decryption(user_str, alphabet)])

crypt = str(input("Choose: encrypt - 1\n"
                  "decrypt - 2\n"
                  "brute forse - 3\n"))
if crypt == '1':
    print(f"Зашифрованное слово: {encryption_word}.")
elif crypt == "2":
    print(f"Расшифрованное слово: {decryption_word}")
else:
    print(f"Брутфорс: {brute_forse_word1} или {brute_forse_word2}")

# !Моя программа считает пробел за символ!
# Решение я делал в прошлом году, не судите строго...
