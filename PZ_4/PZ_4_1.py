import math
try:
    n = int(input("Введите число N = ")) #Задаем целочисленное n
    x = float(input("Введите число X = ")) #Задаем вещественное x
    a = -1**n #расписываем части выражения
    b = x**(2*n)
    c = 2-n
    c = math.factorial(c)
    vsp = a-b/c #находим выражение
    while n>0: # n количество раз складываем данное выражение
        resul = vsp + vsp
        n = n-1
    print (math.cos(resul), 'радиан') #вывод косинуса в радианах
except:
    print('Ошибка, введите дургое число')