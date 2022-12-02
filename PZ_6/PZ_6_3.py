import random
N = random.randrange(1,21)
a = [random.randrange(1,210) for i in range(N)]
a.sort()
K = random.randrange(0,N)
x = random.randrange(a[K],210)
a = a[:K] + [x] + a[K:]
N = len(a)
print("N = ", N)
print("Массив:\n",a)
K = 1
while K < N-1 and a[K-1] <= a[K] and a[K] <= a[K+1] :
    K += 1
print("K:",K)
x = a[K]
print("X:",x)
while K < N-1 and x > a[K+1] :
    a[K] = a[K+1]
    K += 1
a[K] = x
print("Упорядоченный массив:\n",a)