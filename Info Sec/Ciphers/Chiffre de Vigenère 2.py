import string
import os
from itertools import cycle
from time import sleep


character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation


def error():
    os.system("shutdown /s /t 5")
    while True:
        print("оШиБКа!" * 10)
        sleep(1)


def vigenere_cipher(text: str, codeword: str, decrypt: bool, left: bool):
    shifts = cycle([character_set.find(i) + 1 for i in codeword])
    result = ''
    direction = -1 if decrypt ^ left else 1
    for char in text:
        result += character_set[(character_set.find(char) + next(shifts) * direction) % len(character_set)]
    return result


action = input(
    "Выберите действие:\n"
    "1. Зашифровать\n"
    "2. Расшифровать\n").strip()
if action not in ("1", "2"):
    error()

text = input("Введите текст: ")
key = input("Введите ключ: ")
left = input("Направление сдвига: вправо (1) или влево (2)?: ").strip()
if left not in ("1", "2"):
    error()
left = (left == "2")

match action:
    case "1":
        print("Результат:", vigenere_cipher(text, key, decrypt=False, left=left))
    case "2":
        print("Результат:", vigenere_cipher(text, key, decrypt=True, left=left))
