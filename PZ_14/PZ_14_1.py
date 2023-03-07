#Из текстового файла (writer.txt) выбрать фамилии писателей, посчитать количество
#фамилий. Создать новый файл, в котором выполнить замену слова «роман» на слово
#«произведение».

import re
openfile = open('writer.txt', encoding='UTF-8') #Открываем исходный файл
read = openfile.read()
openfile.close()

text_re = re.findall(r"\n[А-Яа-я]+", read) #Вывод всех фамилий писателей
a=len(text_re)
print('Количество фамилий:',a)

old = 'роман '
new = 'произведение '

proizv = read.replace(old, new) #Замена слова «роман» на слово «произведение»

condition = open('proizvedenie.txt', 'w') #Создаём новый файл
condition.write(f'{proizv}')
condition.close()

