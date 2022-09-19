def Check_5(text:str) -> bool:
    check = False
    for i in text:
        if i == '5':
            check = True
            return check
    return check

dictionary = \
{
 'а': 'А',
 'б': 'Б',
 'в': 'В',
 'г': 'Г',
 'д': 'Д',
 'е': 'Е',
 'ж': 'Ж',
 'з': 'З',
 'и': 'И',
 'й': 'Й',
 'к': 'К',
 'л': 'Л',
 'м': 'М',
 'н': 'Н',
 'о': 'О',
 'п': 'П',
 'р': 'Р',
 'с': 'С',
 'т': 'Т',
 'у': 'У',
 'ф': 'Ф',
 'х': 'Х',
 'ц': 'Ц',
 'ч': 'Ч',
 'ш': 'Ш',
 'щ': 'Щ',
 'ъ': 'Ъ',
 'ы': 'Ы',
 'ь': 'Ь',
 'э': 'Э',
 'ю': 'Ю',
 'я': 'Я'
}

def Proccesing(text2) -> list:
    '''
    Метод возвращает измененный список
    '''
    result = []
    for i in text2:
        check = Check_5(i)
        if check:
            result2 = ""
            line = list(i)
            for k in line:
                check2 = False
                for j in dictionary.keys():
                    if k == j:
                        check2 = True
                        break
                if check2:
                    result2 += dictionary[k]
                else:
                    result2 += k
            result.append(result2)
        else:
            result.append(i)
    return result


def Compression(name_file:str) -> str:
    '''
    Метод считает текст из файла, сожмет его и запишет в новый файл
    '''
    text = ""
    listi = []

    y = open(name_file, 'r')
    for line in y:
        text += line
    y.close()

    result = []
    result2 = ""
    listi = text.split(" ")
 #   print(listi)
    i = 0
    while i < len(listi):
        conteiner = listi[i]
        cout = 1
        cont = ""
        j = 0
        while j < len(conteiner):  # Итерирую по каждой букве
            
            prov = True
            for l in cont:   # Проверяю на повторение
                if l == conteiner[j]:
                    prov = False

            if cout != 1 and conteiner[j] != conteiner[j - 1]: # Если счетчик больше 1 и данная буква не такая же как и предыдущая, записываю счетчик и сбрасываю его
                cont += str(cout)
                cout = 1

            if prov or j == 0: # Если нет повторения или если это первая буква слова, записываю ее
                cont += conteiner[j]
            if prov == False:
                cout += 1

            if j == len(conteiner) - 1: # Если слово кончилось, добавляю пробел
                cont += " "
            
            j += 1
        result.append(cont)
        i += 1
    for slovo in result:
        result2 += slovo + " "
 #   print(result2)

    with open('file4.txt', 'w') as data:
        data.write(result2)

    return 'file4.txt'

def De_Compression(name_fil:str):
    '''
    Метод считает текст из файла, восстановит его и перезапишет в этот же файл
    '''
    text = ""
    result2 = ""
    cont = ""
    listi = []

    y = open(name_fil, 'r')
    for line in y:
        text += line
    y.close()

    listi = text.split(" ")
    for i in listi:
        conteiner = i
        result = []
        cout = 0
        j = 0
        ind = 0
        while j < len(conteiner):
            if conteiner[j].isdigit():
                cont += conteiner[j]

            if not conteiner[j].isdigit() and cout != 0 and cont.isdigit():
                cout = 0
                result[ind] = result[ind] * int(cont)
                cont = ""

            if not conteiner[j].isdigit():
                result.append(conteiner[j])
                cout += 1
                ind = len(result) - 1

            if j == len(conteiner) - 1:
                for qw in result:
                    result2 += qw
                result2 += " "
            j += 1
    print(result2)

    with open(name_fil, 'w') as data:
        data.write(result2)
            


# De_Compression(Compression('file3.txt'))