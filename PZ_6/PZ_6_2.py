import random

N = random.randrange(2,21)
a = [random.randrange(1,10) for i in range(N)]

print("N:",N)
print("Массив:",a)

n_repeat = 1
item = a[0]
for i in range(0,N-1) :
    n_tmp = 1
    for j in range(i+1,N) :
        if a[i] == a[j] :
            n_tmp += 1
    if n_repeat < n_tmp :
        n_repeat = n_tmp
        item = a[i]

print("Максимальное количество повторений:", n_repeat)
print("Максимально повторяющееся число:", item)