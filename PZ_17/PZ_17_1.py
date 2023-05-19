# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения.

class Schet:
    def __init__(self, name, surname, znach):
        self.name = name
        self.surname = surname
        self.znach = znach

    def inkrement(self):
        return self.znach + 1

    def dekrement(self):
        return self.znach - 1

per_1 = Schet('Dianne', 'Payne', 5)

print('Инкремент: ',per_1.inkrement())
print('Декремент: ',per_1.dekrement())