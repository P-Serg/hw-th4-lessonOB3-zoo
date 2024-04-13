class Animal: # создание базового класса животные
    def __init__(self, name, age): # создание атрибутов базового класса
        self.name = name
        self.age = age

    def make_sound(self): # создание метода голоса животного
        pass

    def eat(self): # создание метода животное ест
        pass


class Bird(Animal):  # создание подкласса Bird
    def __init__(self, name, age, wingspan):  # создание атрибутов подкласса
        super().__init__(name, age)  # вызов метода родительского класса
        self.wingspan = wingspan  # создание специфичного атрибута подкласса

    def make_sound(self):  # создание метода голоса птицы
        return "Карамба"


class Mammal(Animal):  # создание подкласса млекопитающие
    def __init__(self, name, age, fur_color):  # создание атрибутов подкласса
        super().__init__(name, age)  # вызов метода родительского класса
        self.fur_color = fur_color  # создание специфичного атрибута подкласса

    def make_sound(self): # создание метода голоса млекопитающего
        return "Рррррр"


class Reptile(Animal): # создание подкласса рептилии
    def __init__(self, name, age, scale_color): # создание атрибутов подкласса рептилии
        super().__init__(name, age)  # вызов метода родительского класса
        self.scale_color = scale_color  # создание специфичного атрибута подкласса

    def make_sound(self): # создание метода голоса рептилии
        return "Сссссс"


def animal_sound(animals):  # функция голоса животных
    for animal in animals:  # проход по списку животных
        print(animal.make_sound())  # вывод метода голоса животного


class Zoo:  # создание класса зоопарк
    def __init__(self): # создание атрибутов
        self.animals = [] # создание списка животных
        self.staff = [] # создание списка сотрудников

    def add_animal(self, animal): # добавление животных в зоопарк
        self.animals.append(animal) # добавление животного в список животных

    def add_staff(self, staff): # добавление сотрудников в класс зоопарк
        self.staff.append(staff) # добавление сотрудника в список сотрудников


class ZooKeeper: # создание класса смотритель зоопарка
    def __init__(self, name): # создание атрибутов сотрудника смотритель зоопарка
        self.name = name # создание специфичного атрибута имя сотрудника

    def feed_animal(self, animal): # добавление животного в список животных сотрудника смотрителя зоопарка
        print(f"{self.name} кормит {animal.name}") # вывод метода голоса животного


class Veterinarian: # создание класса ветеринар
    def __init__(self, name):    # создание атрибутов сотрудника ветеринар
        self.name = name # создание специфичного атрибута имя сотрудника ветеринара

    def heal_animal(self, animal): # добавление животного в список животных сотрудника ветеринара
        print(f"{self.name} лечит {animal.name}")  # вывод метода голоса животного




bird = Bird("Попугай", 5, "зеленые")
mammal = Mammal("Лев", 3, "Желтый")
reptile = Reptile("Змея", 2, "Коричневая")

zookeeper = ZooKeeper("Иван")
veterinarian = Veterinarian("Семен Петрович")

zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

for staff_member in zoo.staff:
    if isinstance(staff_member, ZooKeeper):
        staff_member.feed_animal(bird)
    elif isinstance(staff_member, Veterinarian):
        staff_member.heal_animal(mammal)

animal_sound([bird, mammal, reptile])
