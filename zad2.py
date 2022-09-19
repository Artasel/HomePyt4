# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from random import randint

list = []
i = 0
while i < 15:
    list.append(randint(1, 10))
    i += 1
print(list)

def Del_Repet(x:list) -> list:
    '''
    Метод запишет в новый список данные из списка-аргумента, повторяющиеся запишет в единственном экземпляре
    '''
    list = []
    for i in x:
        prov = True
        for j in list:
            if i == j:
                prov = False
        if prov:
            list.append(i)
    return list

print(Del_Repet(list))