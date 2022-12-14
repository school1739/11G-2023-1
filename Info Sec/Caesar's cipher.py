alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def cipher_encrypt(alf, text, key):
    encrypted = ""
    for i in text:
        if i.upper() in alf:
            i = i.upper()
            index = alf.find(i)
            new_index = index + key
            encrypted += alf[new_index]
        else:
            encrypted+=i
    return encrypted


def brute_force(alf, text):
    for key in range(1, len(alf) + 1):
        encrypted = ""
        for i in text:
            i = i.upper()
            index = alf.find(i)
            new_index = index - key - 1
            encrypted += alf[new_index]
        print(encrypted)


def cipher_decrypt(alf, text, key):
    decrypted = ""
    for i in text:
        index = text.find(i.upper())
        new_index = index - key + 2
        decrypted += alf[new_index]

    return decrypted


alf = input("Выберите язык: RU - 1\n"
            "EN - 2\n")

crypt = input("Выберите: зашифровать - 1\n"
              "расшифровать - 2\n"
              "перебор - 3\n")

text = str(input("Введите текст: \n"))
try:
    key = int(input("Введите ключ(если есть): \n"))
except ValueError:
    pass
if str(alf) == '1':
    alf = alfavit_RU
else:
    alf = alfavit_EU
if str(crypt) == "1":
    print(cipher_encrypt(alf, text, key))
elif str(crypt) == "2":
    print(cipher_decrypt(alf, text, key))
else:
    print(brute_force(alf, text))
