
# TODO: Подробно описать три произвольных класса

import doctest

# TODO: описать класс

class cat:

    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса "cat":
        :param name: имя кота (str)
        :param age: Возраст кота (int)
        :param breed: порода кота (str)

        Примеры:
        >>> cat1 = cat("barsik", 3, "britan")   # Инициализация объекта класса
        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None):
        """
        Функция добавления данных в объект

        :param name: имя кота (str)
        :param age: Возраст кота (int)
        :param breed: порода кота (str)
        """
        self.name = name
        if age >= 0:   # Возраст не может быть отрицательным
            self.age = age
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.breed = breed

    def print_data(self):
        print(self.name, self.age, self.breed)

# TODO: описать ещё класс

class student:
    def __init__ (self, surname: str = None, add_sessions: int = 0, is_in_university: bool = False):
        """
        Создание объета класса "student"
        :param surname: фамилия студента
        :param add_sessions: Количество допсессий у студента
        :param is_in_university: Учится ли студент в ВУЗе

        Примеры:
        >>> student1 = student("Ivanov", 1, True)   # Инициализация объекта класса
        """
        self.add_data(surname, add_sessions, is_in_university)

    def add_data (self, surname: str = None, add_sessions: int = 0, is_in_university: bool = None):
        """
        Функция добавления данных о студенте

        :param surname: фамилия студента
        :param add_sessions: Количество допсессий у студента
        :param is_in_university: Учится ли студент в ВУЗе
        """
        self.surname = surname
        if add_sessions >= 0:  # Студент не может иметь отрицательное количество допсессий
            self.add_sessions = add_sessions
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.is_in_university = is_in_university
        if self.add_sessions > 5:        # Если количество допсессий больше 5-ти, студент считается отчисленным
            self.is_in_university = False



# TODO: и ещё один
class prepod:
    def __init__(self, surname: str = None, umber_of_students_expelled: int = None):
        """
        Создание объекта класса "prepod"
        :param surname: Фамилия преподавателя
        :param umber_of_students_expelled: Количество отчисленных этим преподавателем студентов

        Примеры:
        >>> prepod1 = prepod("Zelikman", 18634)
        """
        self.add_data(surname, umber_of_students_expelled)

    def add_data(self, surname: str = None, number_of_students_expelled: int = None):
        """
        Функция добавления данных о преподавателе
        :param surname: Фамилия преподавателя
        :param umber_of_students_expelled: Количество отчисленных этим преподавателем студентов
        """
        self.surname = surname
        if number_of_students_expelled >= 0:
            self.number_of_students_expelled = number_of_students_expelled
        else:
            raise ValueError("Значение не может быть отрицательным")
    def print_data(self):
        """
        Функция вывода данных о преподавателе
        """
        print(self.surname, self.number_of_students_expelled)