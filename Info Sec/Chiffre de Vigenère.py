# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  # 0 - 32
alphabet_EU = ' ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 0 - 25

# HINT (использовать не обязательно):
# Если буквы A-Z соответствуют числам 0-25, то код Виженера в общем виде выглядит так:
#   Шифрование:
#       Ci=(Pi+Ki) mod 26
#   Расшифровка:
#       Pi=(Ci-Ki+26) mod 26

language = int(input(
    "Введите цифру языка, на котором вы напишите слово | Enter number of language, on which you will write a word (RU - 1, EU - 2): "))

if language == 1:
    keywordRU = input("Введите ключевое слово (только заглавными буквами): ")  # Просим ввести ключевое слово
    wordRU = input(
        "Введите слово, которое хотите зашифровать (только заглавными буквами): ")  # Просим ввести само слово для шифровки
    keywordRU_spisok = []  # Список для индекса ключевого слова
    wordRU_spisok = []  # Список для индекса слова для шифровки

    for b in keywordRU:  # Находим индексы букв ключевого слова и складываем в список
        keywordRU_index = int(alphabet_RU.find(b))
        keywordRU_spisok.append(keywordRU_index)

    for c in wordRU:  # Находим индексы букв слова для шифровки и складываем в список
        if c == " ":
            wordRU_spisok.append(0)
            continue
        else:
            wordRU_index = int(alphabet_RU.find(c))
            wordRU_spisok.append(wordRU_index)

    for i in range(len(wordRU_spisok)):  # По очереди складываем индексы из слова для шифровки и ключевого слова
        if wordRU_spisok[i] == 0:
            print(" ", end="")
        else:
            sum = wordRU_spisok[i] + keywordRU_spisok[i % len(keywordRU_spisok)]
            print(alphabet_RU[sum],
                end="")  # Получаем зашифрованное слово. Шифровка предложений, дешифровка, защита от дурака и версия с английскими словами приняла ислам



elif language == 2:
    keyword2 = input("Enter keyword: ")
else:
    print("Неправильно! Попробуй ещё раз | Wrong! Try again")
    language = int(input(
        "Введите цифру языка, на котором вы напишите слово | Enter number of language, on which you will write a word (RU - 1, EU - 2): "))
