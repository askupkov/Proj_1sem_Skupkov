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

    for i in range(0, K - 1):
        sum+= a[i]
    for i in range(L, N):
        sum+= a[i]

    c = sum/((K-1)+(N-L))
    print('Среднее арифметическое элементов = ', c)
except:
    print('Вы ввели недопустимое значение переменной')