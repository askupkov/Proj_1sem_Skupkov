#Дан список размера N и целые числа K и L (1 < K < L < N ). Найти среднее арифметическое элементов список с номерами от K до L включительно.
try:
    a = []
    sum = 0
    N = int(input("Введите размер списка N= "))

    print('Заполните список целыми числами')
    for i in range(N):
        a.append(int(input("A= ")))

    print('Ваш список', a)

    print('Введите K и L при условии 1<K<L<N')
    K = int(input("K= "))
    L = int(input("L= "))

    for i in range((K-1), (L)):
        sum+= a[i]

    c = sum/(L-K+1)
    print('Среднее арифметическое элементов = ', c)
except:
    print('Вы ввели недопустимое значение переменной')