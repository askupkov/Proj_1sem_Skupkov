import random
A = random.randrange(-100,100) #Генерация случайного числа A
B = random.randrange(-100,100) #Генерация случайного числа B
print('Даны два числа, выведено сначало большее потом меньшее')
if A>B:
    print('Число A больше B')
    print(A)
    print(B)
elif A==B:
    print('Числа A и B равны')
else:
    print('Число B больше A')
    print(B)
    print(A)