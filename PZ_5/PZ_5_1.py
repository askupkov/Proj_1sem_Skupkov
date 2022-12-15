#Составить функцию, которая напечатает сорок любых символов
import random
import string

print('Функция напечатает 40 рандомных символов:')
def random_string(length): #функция которая создаёт рандомный символ
    letter = string.ascii_letters
    random.str = ''.join(random.choice(letter) for i in range(length))
    print(random.str)

random_string(40) #находим 40 рандомных символов