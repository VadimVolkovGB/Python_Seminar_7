
# def f(x):
#     return x
# print(f(5))
#
# Y = lambda x: x
# print(Y(5))

# list1 = ['1', '2', '3']
# list1 = list(map(int, list1))
# print(list1)

# list1 = '1 2 3'
# list1 = list(map(int, input().split()))
# print(list1)

# a = ('a', 'b', '2', '3', 'c')
# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)
# print(*b)
# print(*c)

# У вас есть код, который вы не можете менять
# (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего
# сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] #
# или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом
# - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно
# никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation,
# чтобы transformed_values получился
# копией values.

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformed_values = list(map(lambda x: x*2, values))
# print(values)
# print(transformed_values)

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# c = filter(lambda x: x[0]!= x[1], orbits)
# f = list(map(lambda x: x[0]* x[1], c))
# print(f)
# print(c)

# или

# def find_f_orbit(orbits):
#     areas = [a*b for a, b in orbits]
#     max_area = areas.index(max(areas))
#     return orbits[max_area]
# print(*find_f_orbit(orbits))

# или

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(max(orbits, key=lambda x: x[0]* x[1] * (x[0] != x[1])))


# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

# def rhythm(str):
#     str = str.split()
#     list_1 = []
#     for word in str:
#         sum_w = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum_w += 1
#         list_1.append(sum_w)
#     return len(list_1) == list_1.count(list_1[0])
#
# str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# if rhythm(str_1):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f"{x:>3}" for x in i])
#
#
# print_operation_table(lambda x, y: x * y)