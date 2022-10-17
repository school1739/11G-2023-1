import string

character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation


def cipher_cipher(text, key, decrypt=False):
    if key < 0:
        print("key cannot be negative")
        return None
    n = len(character_set)
    if decrypt:
        key = n - key
    table = str.maketrans(character_set, character_set[key:]+character_set[:key])
    translated_text = text.translate(table)
    return translated_text


action = int(input("Выберите действие:\n"
                   "1. Зашифровать\n"
                   "2. Расшифровать\n"
                   "3. Брутфорс\n"))

text = input("Введите текст: ")
if action in (1, 2):
    key = int(input("Введите ключ: "))

result = ""
match action:
    case 1:
        print("Результат:", cipher_cipher(text, key))
    case 2:
        print("Результат:", cipher_cipher(text, key, decrypt=True))
    case 3:
        for key, _ in enumerate(character_set):
            print(f"key '{key}':", cipher_cipher(text, key, decrypt=True))


