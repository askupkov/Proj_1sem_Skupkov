#Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^N.
n=int(input('Введите целое число, больше нуля. n: ')) #вводим число до которого будет идти цикл
i=1 #число, начиная с которого будет производится сумма
p=0 #объявляем вспомогательную переменную
while n>=i: #нахождение суммы
    p=p+i**i
    i=i+1
print('Сумма равна ', p) #вывод суммы