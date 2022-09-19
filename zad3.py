# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
# которые имеют средний балл более «4».

import prov


with open('file.txt', 'w') as data:
    data.write('Ангела Меркель 5\n')
    data.write('Андрей Валетов 5\n')
    data.write('Фредди Меркури 1\n')
    data.write('Анастасия Пономарева 4\n')
    data.write('Цезарь Федорович 2\n')
    data.write('Юлий Долгорукий 3\n')
    data.write('Артазель Мирович 4\n')
    data.write('Тарас Бульбович 5\n')

list = []
y = open('file.txt', 'r') # Создаем список
for line in y:
    list.append(line)
y.close()

list = prov.Proccesing(list) # Изменяем список согласно заданию

with open('file.txt', 'w') as data: # Перезаписываем файл
    for i in list:
        data.write(i)

read_file = open('file.txt', 'r')  # Читаем файл
for line in read_file:
    print(line)
read_file.close()