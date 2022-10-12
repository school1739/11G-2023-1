import string

character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation

def cipher_cipher_using_lookup(text,  key, decrypt=False):
    if key < 0:
        print("key cannot be negative")
        return None
    n = len(character_set)
    if decrypt:
        key = n - key
    table = str.maketrans(character_set, character_set[key:]+character_set[:key])
    translated_text = text.translate(table)
    return translated_text

print("Выберите действие:")
print("1.Зашифровать 2.Расшифровать 3.Брутфорс")
human_answer = int(input())
result = ""

if human_answer == 1:
    text = input("Введите текст для шифровки: ")
    key = int(input("Введите ключ для шифровки: "))
    print("Результат шифровки:", cipher_cipher_using_lookup(text, key))
elif human_answer == 2:
    text = input("Введите текст для дешифровки: ")
    key = int(input("Введите ключ для дешифровки: "))
    print("Результат дешивровки:", cipher_cipher_using_lookup(text, key, decrypt=True))
elif human_answer == 3:
    text = input("Введите текст для шифровки: ")
    key = int(input("Введите ключ для шифровки: "))
    for key, _ in enumerate(character_set):
        print(f"key '{key}':", cipher_cipher_using_lookup(text, key, decrypt=True))