# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

from random import randint

def Prov_Prost_Numb(x:int) -> bool:
    '''
    Функция проверяет x, является ли оно проcтым множителем
    '''
    prov = True
    i = 2
    while i <= x:
        if x % i == 0 and i != 1 and i != x:
            prov = False
            return prov
        i += 1
    return prov

N = randint(10, 1000)
print(N)
list = []
i = 2
while i <= N:
    if N % i == 0:
        prov = Prov_Prost_Numb(i)
        if prov:
            list.append(i)
    i += 1

print(list)