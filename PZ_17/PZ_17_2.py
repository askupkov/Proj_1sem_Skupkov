# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы".

class Rabotnik: #базовый класс работник
    def __init__(self, name):
        self.name = name

    def work(self): # общие методы
        print(f"{self.name} работает")

    def get_paid(self):
        print(f"{self.name} получает зарплату")

class Manager(Rabotnik): #дочерние классы
    def manage_team(self):
        print(f"{self.name} управляет командой")

class Engineer(Rabotnik):
    def designs_systems(self):
        print(f"{self.name} проектирует системы")

Manager = Manager('Анатолий')
Engineer = Engineer('Игорь')

Manager.work()
Engineer.work()

Manager.manage_team()
Engineer.designs_systems()

Manager.get_paid()
Engineer.get_paid()