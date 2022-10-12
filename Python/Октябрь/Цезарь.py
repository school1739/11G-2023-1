shift = 3 # определение количества сдвигов
text = "ITS BRITNEY BITCH"
encryption = ""
for c in text: #заглавная ли буква
    if c.isupper(): # найти положение в 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A") # выполнить перестановку
        new_index = (c_index + shift) % 26 # преобразовать в новый символ
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode) # добавление к зашифрованной строке
        encryption = encryption + new_character
    else:
        # так как символ не является строчным, оставляем его как есть
        encryption += c
print("Plain text:",text)
print("Encrypted text:",encryption)