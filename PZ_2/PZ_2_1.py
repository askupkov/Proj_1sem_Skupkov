#Дано трехзначное число. Вывести число, полученное при перестановке цифр сотен и десятков исходного числа (например, 123 перейдет в 213).
try:
    a=int(input('Введите трёхзначное целое число: ')) #Ввод исходного числа
    b=a//100 #Нахождение сотен
    c=a%100//10 #Нахождение десятков
    d=a%10 #Нахождение единиц
    print('Число полученное при перестановке цифр сотен и десятков:',c*100+b*10+d) #Вывод конечного числа
except ValueError:
    print('Введите трёхзначное число')