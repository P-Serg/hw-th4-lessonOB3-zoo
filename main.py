# hw-th4-lessonOB3-zoo

import pickle  # импорт модуля pickle для сохранения данных в файл

class Animal(): # создание базового класса животного
    def __init__(self, name, age): # создание атрибутов базового класса животного
        self.name = name # создание специфичного атрибута имя животного
        self.age = age # создание специфичного атрибута возраст животного

    def make_sound(self): # создание метода голоса животного
        pass

    def eat(self):  # создание метода животное ест
        pass


class Bird(Animal):  # создание подкласса птицы
    def __init__(self, name, age, wingspan):  # создание атрибутов подкласса птицы
        super().__init__(name, age)  # вызов метода родительского класса
        self.wingspan = wingspan  # создание специфичного атрибута птицы

    def make_sound(self):  # создание метода голоса птицы
        return "Карамба"


class Mammal(Animal):  # создание подкласса млекопитающих
    def __init__(self, name, age, fur_color):  # создание атрибутов подкласса млекопитающих
        super().__init__(name, age)  # вызов метода родительского класса
        self.fur_color = fur_color  # создание специфичного атрибута млекопитающих

    def make_sound(self):  # создание метода голоса млекопитающих
        return "Рррр"


class Reptile(Animal):  # создание подкласса рептилий
    def __init__(self, name, age, scale_color):  # создание атрибутов подкласса рептилий
        super().__init__(name, age)  # вызов метода родительского класса
        self.scale_color = scale_color  # создание специфичного атрибута рептилий

    def make_sound(self):  # создание метода голоса рептилий
        return "Сссс"


def animal_sound(animals):  # функция голоса животных
    for animal in animals:  # проход по списку животных
        print(animal.make_sound())  # вывод метода голоса животного


class Zoo:  # создание класса зоопарк
    def __init__(self):  # создание атрибутов
        self.animals = []  # создание списка животных
        self.staff = []  # создание списка персонала

    def add_animal(self, animal):   # добавление животных в зоопарк
        self.animals.append(animal)

    def add_staff(self, staff):  # добавление сотрудников в класс зоопарк
        self.staff.append(staff)

    def save_zoo(self, filename):  # сохранение данных в файл
        with open(filename, 'wb') as file: # запись данных в файл
            pickle.dump(self, file)

    def load_zoo(filename):  # загрузка данных из файл
        with open(filename, 'rb') as file: # чтение данных из файл
            return pickle.load(file)


class ZooKeeper:  # создание подкласса сотрудников смотритель зоопарка
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal): #  кормление животного
        print(f"{self.name} кормит {animal.name}")


class Veterinarian:  # создание подкласса сотрудников ветеринар зоопарка
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal): # лечение животного
        print(f"{self.name} лечит {animal.name}")


# Создаем зоопарк и добавляем животных и персонал
zoo = Zoo()
bird = Bird("Попугай", 5, "зеленый")
mammal = Mammal("Лев", 3, "желтый")
reptile = Reptile("Змея", 2, "коричневый")
bird1 = Bird("Павлин", 4, "синий")
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_animal(bird1)

zookeeper = ZooKeeper("Иван")
veterinarian = Veterinarian("Семен Петрович")
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Сохраняем зоопарк в файл
zoo.save_zoo("zoo.pkl")

# Загружаем зоопарк из файла
loaded_zoo = Zoo.load_zoo("zoo.pkl")

# Выводим информацию о загруженном зоопарке
print("Животные в зоопарке:")
for animal in loaded_zoo.animals:
    print(f"{animal.name} - {type(animal).__name__}")
print("Сотрудники зоопарка:")
for staff in loaded_zoo.staff:
    print(staff.name)
