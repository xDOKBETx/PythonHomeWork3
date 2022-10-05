# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def convert_decimal_to_binary(number):
    binary_number = ""
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number //= 2
    return binary_number


decimal_number = int(input("Введите натуральное целое число: "))
print(convert_decimal_to_binary(decimal_number))
