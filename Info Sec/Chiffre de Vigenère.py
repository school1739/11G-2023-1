# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' #0 - 32
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' #0 - 25

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26

lan = int(input("Введите цифру языка, на котором вы напишите слово | Enter number of language, on which you will write a word (RU - 1, EU - 2): "))

if lan == 1:
    keyword1 = input("Введите ключевое слово: ")
    word1 = input("Введите слово, которое хотите зашифровать: ")
    a = len(word1)
    for a in word1:
        for b in keyword1:
            word_index = alphabet_RU.find(b)
            word_index = int(word_index + 1)
        for c in word1:
            word1 = str(alphabet_RU.find(c))
            word1new = int(word1) + 1
        print(alphabet_RU[word_index + word1new], sep="")

elif lan == 2:
    keyword2 = input("Enter keyword: ")
else:
    print("Неправильно! Попробуй ещё раз | Wrong! Try again")
    lan = int(input(
        "Введите цифру языка, на котором вы напишите слово | Enter number of language, on which you will write a word (RU - 1, EU - 2): "))

