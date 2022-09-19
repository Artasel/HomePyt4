# Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит 
# обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и 
# дешифровывает его.

text = "Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо."

def Encrypt_Left(stroka:str, key:int) -> str:
    finall = ""
    cont = []
    cont = stroka.split(" ") # Создал список
    i = 0
    while i < len(cont):   # итерирую по списку
        contain = ""
        result = ""
        result2 = []
        iter = []
        contain = cont[i]
        if len(contain) > 1:  # если текст длиннее одного знака
            iter = list(contain)
            l = 0
            while l < key: # итерирую влево столько раз, сколько указано в key
                if result2 != []:
                    iter = result2
                    result2 = []
                j = 0
                while j < len(contain):
                    if j != len(contain) - 1:
                        result2.append(iter[j + 1])
                    else:
                        result2.append(iter[0])
                    j += 1
                l += 1
            for zn in result2:
                result += zn
            finall += result + " "
        else:
            finall += contain + " "
        i += 1
    fil = 'file2.txt'
    with open(fil, 'w') as data: # записываем файл
        for qw in finall:
            data.write(qw)
    print(finall)
    return fil

def Decipher(name_file:str):
    key = int(input("Какой ключ шифрования?: "))

    strin = ""
    read_file = open(name_file, 'r')  # Создаем строку
    for line in read_file:
        strin += line
    read_file.close()

    list = []
    list = strin.split(" ")  # Создаем список

    final = ""
    i = 0
    while i < len(list):
        list2 = []
        list2 = list[i]
        if len(list2) > 1:
            q = 0
            while q < key:
                list3 = ""
                for l in list2:
                    list3 += l
                list2 = []
                cont = list3[len(list3) - 1]
                w = 0
                while w < len(list3):
                    if w == 0:
                        list2.append(cont)
                    else:
                        list2.append(list3[w - 1])
                    w += 1
                q += 1
            for p in list2:
                final += p
            final += " "
        else:
            final += list2 + " "
        i += 1
    print(final)

qwe = Encrypt_Left(text, 3)
Decipher(qwe)