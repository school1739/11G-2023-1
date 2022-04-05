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

def encrypt(plain_text, alphabet):
    changes = [alphabet.find(i) + 1 for i in key]
    output = ''
    for i, j in enumerate(plain_text):
        shift = changes[i % len(changes)]
        if j == ' ':
            output += ' '
        else:
            output += alphabet[(alphabet.find(j) + shift) % len(alphabet)]
    print(output.lower())


def decrypt(encrypted_text, alphabet):
    changes = [alphabet.find(i) + 1 for i in key]
    output = ''
    for i, j in enumerate(encrypted_text):
        shift = changes[i % len(changes)]
        if j == ' ':
            output += ' '
        else:
            output += alphabet[(alphabet.find(j) - shift) % len(alphabet)]
    print(output.lower())


language = input("language: 'ru' or 'eng' -  ")

if language == "ru":
    alphabet = alphabet_RU
elif language == "eng":
    alphabet = alphabet_EU
else:
    print("I dunno this language :(")

what_do_u_wanna = input("pls say me, what do u wanna: 'encrypt' or 'decrypt'...  ")
print("Okay...")

if what_do_u_wanna == "encrypt":
    text = input("Then enter the text you want to encrypt:  ").upper()
    key = input("And pls enter the key of encrypt:  ").upper()
    encrypt(text, alphabet)
elif what_do_u_wanna == "decrypt":
    text = input("Then enter the text you want to decrypt:  ").upper()
    key = input("And pls enter the key of decrypt:  ").upper()
    decrypt(text, alphabet)
else:
    print("Are u dummy? WTF do u wanna?")


