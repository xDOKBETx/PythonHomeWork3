# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

n = int(input("Введите количество элементов в списке: "))
list_of_elements = [random.randint(1, 10) for _ in range(n)]


def multiplication_elements(ls):
    res = []
    for i in range((len(ls) + 1) // 2):
        res.append(ls[i] * ls[len(ls) - 1 - i])
    return res


print(list_of_elements, end=" =>")
print(multiplication_elements(list_of_elements))
