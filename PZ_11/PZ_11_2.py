# Из предложенного текстового файла (text18-20.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить строку
# наибольшей длины.

sum=0
w = 0
a = 0

for i in open('text18-20.txt', encoding='UTF-8'):
    print(i, end='') #вывод содержимого текстового файла
    sum=sum+len(i)
    if len(i)>a:
        a=len(i)
        m=i

print(end='\n')
print(end='\n')

print('Количество символов в тексте: ',sum)

f1 = open('text18-20-2.txt', 'w') #создаём новый файл
f1.writelines(m)
f1.close()