# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26
"""
plain_text=input("Plain: ")
key_text=input("Key: ")
for key_char in plain_text:
    key_index=alphabet_RU.find(key_char)
    print(key_index+1)                    #индекс ключа

for plain_char in plain_text:
    plaint_index=alphabet_RU.find(plain_char)
    print(plaint_index+1)

for char in (plain_text):
    print(alphabet_RU[plaint_index+key_index])
"""
from itertools import cycle

LEN = 127


def full_encode(value, key):
    return ''.join(map(lambda x: chr((ord(x[0]) + ord(x[1])) % LEN), zip(value, cycle(key))))


def full_decode(value, key):
    return ''.join(map(lambda x: chr((ord(x[0]) - ord(x[1]) + LEN) % LEN), zip(value, cycle(key))))


if __name__ == "__main__":
    word = input()
    key = input()

    print ('Слово: ' + word)
    print ('Ключ: ' + key)

    shifre = full_encode(word, key)
    print ('Шифр=', shifre)

    decoded = full_decode(shifre, key)
    print ('Word=', decoded)