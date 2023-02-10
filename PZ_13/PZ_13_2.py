#В матрице найти минимальный и максимальные элементы.
import random
a=0
l=0
M=random.randint(2, 9)
N=random.randint(2, 9)
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]

print('Матрица: ')
for i in range(N):
  print(matrix[i])
print('\n')
print('Максимальный элемент:')
for i in range(N):
  b=matrix[l]
  b=max(b)
  l=l+1
  if b>a:
    a=b
print(a)

l=0
print('\n')
print('Минимальный элемент:')
for i in range(N):
  b=matrix[l]
  b=min(b)
  l=l+1
  if b<a:
    a=b
print(a)