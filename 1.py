# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной  позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_of_elements_odd_position():
    result = 0
    for i in range(1, len(list_of_elements), 2):
        result += list_of_elements[i]
    return result


try:
    list_of_elements = [int(i) for i in input("Введите последовательность целых чисел через пробел: ").split()]
    print(list_of_elements)
except:
    print("Нужно вводить целые числа через пробел!")
print(f'\nСумма элементов, стоящих на нечетных позициях: {sum_of_elements_odd_position()}')
