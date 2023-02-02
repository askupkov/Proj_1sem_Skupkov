# В последовательности на n целых элементов в первой ее половине найти
# количество положительных элементов.

import random
n=0
w=0
lst=[]
n1=random.randint(0, 99)
l=n1//2
print('Количество элементов:',n1)
while n1>n:
    number = random.randint(-101, 101)
    lst = lst + [number]
    n = n+1
print(lst)
for i in range(l):
    lst.pop(-1)
for i in lst:
    if i>0:
        w=w+1
print('Количество положительных элементов в первой половине:', w)