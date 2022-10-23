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
def vigenere_cipher(text: str, alphabet: str, encrypt: bool): # Общая функция для шифрования и дешифрования
    shifts = cycle([alphabet.find(i) + 1 for i in codeword])
    result = ''
    for char in text:
        if char not in alphabet:
            result += char
        else:
            x = 1 if encrypt else -1
            result += alphabet[(alphabet.find(char) + next(shifts) * x) % len(alphabet)]
    return result
def encrypt(text: str, alphabet: str): # Обёртка функции для шифрования
    return vigenere_cipher(text, alphabet, True)
def decrypt(text: str, alphabet: str): # Обёртка функции для дешифрования
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
