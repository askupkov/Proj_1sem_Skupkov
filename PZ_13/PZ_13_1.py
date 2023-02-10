#В матрице найти сумму элементов первых двух строк
import random
M=random.randint(2, 9)
N=random.randint(2, 9)
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]

print('Матрица: ')
for i in range(N):
  print(matrix[i])

a=matrix[0]
b=matrix[1]
print('\n')
print('Сумма первых двух строк:')
c = map(sum, zip(a, b))

# вывод результата
print(list(c))