from task_1 import  *   # TODO: импортируйте классы, созданные в ходе выполнения прошлого задани


cat1 = cat("barsik", 5, "Maine coon")
student1 = student("Sidorov", 3, True)
prepod1 = prepod("Zelikman", 18635)

if __name__ == "__main__":

# TODO: инстанцировать все описанные классы, создав три объекта.C()

    try:
    # TODO: вызвать метод с некорректными аргументами(b)
        cat1.add_data(..., -1, ...)
    except:
        print('Ошибка: неправильные данные')

    try:
        student1.add_data(..., ..., 5)
     # TODO: вызвать метод с некорректными аргументами(a)
    except:
        print('Ошибка: неправильные данные')

    try:
        prepod1.add_data(..., -1)
     # TODO: вызвать метод с некорректными аргументами(a)
    except:
        print('Ошибка: неправильные данные')
