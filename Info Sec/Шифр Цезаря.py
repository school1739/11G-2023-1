alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypt = input("Введите слово: ")
key = int(input("Введите цифру позиции на которую сместяться буквы: "))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encrypted = encrypted + alphabet[newPosition]
    else:
        encrypted = encrypted + letter
print(encrypted)

#Для шифрования значение ключа должно быть положительным
#Для дешифрования значение ключа должно быть отрицательным