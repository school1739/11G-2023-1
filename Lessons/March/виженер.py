alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
# Шифрование:
# Ci=(Pi+Ki) mod 26
# Расшифровка:
# Pi=(Ci-Ki+26) mod 26
# C = Cipher Text (зашифрованный текст)
# P = Plain Text (изначальный текст)
# K = Key (ключ)


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
    function = input('Зашифровать или дешифровать? (з/д): ').lower()
    text = input('Ваш текст: ').upper()
    language = input('Выбирите язык (ru/en): ').lower()
    word = input('Какое кодовое слово: ').upper()

    if language == 'ru':
        alphabet = alphabet_RU
    else:
        alphabet = alphabet_EU

    if function == 'д':
        result = decrypt(text, alphabet)
    else:
        result = encrypt(text, alphabet)

    print(f'Результат: {result}\n\n')