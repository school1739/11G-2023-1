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
def endecrypt(text, alphabet, x):
    shifts = [alphabet.find(i) + 1 for i in word]
    result = ''
    for index, char in enumerate(text):
        shift = shifts[index % len(shifts)]
        if char == ' ':
            result += ' '
        else:
            result += alphabet[(alphabet.find(char) + shift * x) % len(alphabet)]
    return result

def encrypt(text, alphabet):
    return endecrypt(text, alphabet, 1)

def decrypt(text, alphabet):
    return endecrypt(text, alphabet, -1)

while True:
    function = input('Зашифровать или дешифровать?: ').lower()
    text = input('Введите текст: ').upper()
    language = input('Введите язык, русский/английский: ').lower()
    word = input('Введите кодовое слово: ').upper()

    if language == 'русский':
        alphabet = alphabet_RU
    else:
        alphabet = alphabet_EU

    if function == 'зашифровать':
        result = encrypt(text, alphabet)
    else:
        result = decrypt(text, alphabet)

    print(f'Результат: {result}\n\n')