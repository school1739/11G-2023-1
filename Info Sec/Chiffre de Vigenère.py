# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...
from itertools import cycle

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26


# Общая функция для шифрования и дешифрования
def vigenere_cipher(text: str, alphabet: str, encrypt: bool):
    shifts = cycle([alphabet.find(i) + 1 for i in codeword])
    result = ''
    for char in text:
        if char not in alphabet:
            result += char
        else:
            x = 1 if encrypt else -1
            result += alphabet[(alphabet.find(char) + next(shifts) * x) % len(alphabet)]
    return result


# Обёртка функции для шифрования
def encrypt(text: str, alphabet: str):
    return vigenere_cipher(text, alphabet, True)


# Обёртка функции для дешифрования
def decrypt(text: str, alphabet: str):
    return vigenere_cipher(text, alphabet, False)


while True:
    language = input('Язык (ru/en): ').lower()
    function = input('Зашифровать или дешифровать (з/д): ').lower()
    text = input('Текст: ').upper()
    codeword = input('Кодовое слово: ').upper()

    if language == 'ru':
        alphabet = alphabet_RU
    else:
        alphabet = alphabet_EU

    if function == 'д':
        result = decrypt(text, alphabet)
    else:
        result = encrypt(text, alphabet)

    print(f'Результат: {result}\n\n')
