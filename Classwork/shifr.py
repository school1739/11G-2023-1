def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d
def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()
#Сначала необходимо создать словарь символов, которые будут участвовать в шифровании:
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
    return dic

def full_encode(value, key):
    dic = comparator(value, key)
    print 'Compare full encode', dic
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis
#Дальше необходимо сопоставить буквы в нашем слове с буквами в словаре и присвоить им соответствующие числовые индексы
def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code
def full_decode(value, key):
    dic = comparator(value, key)
    print 'Deshifre=', dic
    d = form_dict()
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go)
    return lis
#Получаем наш индексы шифра и переводим их в строку функцией decode_val():

{0: [72, 107], 1: [101, 101], 2: [108, 121], 3: [108, 107], 4: [111, 101], 5: [32, 121], 6: [119, 107], 7: [111, 101], 8: [114, 121], 9: [108, 107], 10: [100, 101]}

Индексы: [52, 75, 102, 88, 85, 26, 99, 85, 108, 88, 74]

Получаем закодированное суперсекретное послание: 4KfXUcUlXJ

Раскодировать же все это можно с помощью функции full_decode(), первым аргументом которой есть список числовых индексов шифра, а вторым — список индексов ключа:


if __name__ == "__main__":
    word = 'Hello world'
    key = 'key'

    print
    'Слово: ' + word
    print
    'Ключ: ' + key

    key_encoded = encode_val(key)
    value_encoded = encode_val(word)

    print
    'Value= ', value_encoded
    print
    'Key= ', key_encoded

    shifre = full_encode(value_encoded, key_encoded)
    print
    'Шифр=', ''.join(decode_val(shifre))

    decoded = full_decode(shifre, key_encoded)
    print
    'Decode list=', decoded
    decode_word_list = decode_val(decoded)
    print
    'Word=', ''.join(decode_word_list)
#Все так же получаем индексы шифра и переводим их в строку уже знакомой функцией decode_val():
[72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
И вуаля! Наше зашифрованное слово: Hello world
