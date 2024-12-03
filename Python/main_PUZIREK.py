# BUBLE_SORT пузырьковый метод сортировки

# from random import randint
# numbers = [randint(1, 20) for i in range(10)]
# print(numbers)
#
# n = len(numbers)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j],numbers[j + 1] = numbers[j + 1], numbers[j]
#
# print(f"Отсортированнный список: {numbers}")

# QUICK_SORT быстрая сортировка

# from random import randint
# numbers = [randint(1, 20) for i in range(10)]
# print(numbers)
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [i for i in arr if i < pivot]
#     right = [i for i in arr if i > pivot]
#     midle = [i for i in arr if i == pivot]
#     return quick_sort(left) + midle + quick_sort(right)
#
# print(f"Отсортированнный список: {quick_sort(numbers)}")

# LINE_SEARCH линейный поиск

# from random import randint
# numbers = [randint(1, 20) for i in range(10)]
# print(numbers)
# def liner_search(arr, element):
#     for i in range(len(arr)):
#         if arr[i] == element:
#             return i
#     return -1
#
# find_number = int(input("Введите число для поиска: "))
# if liner_search(numbers, find_number) != -1:
#     print(f"Элемент {find_number} найден в списке")

# BINAR_SEARCH бинарный поиск

from random import randint
numbers = sorted([randint(1, 20) for i in range(10)])
print(numbers)

def binary_serch(arr, element):
    left = 0
    right = len(arr) - 1
    while left <= right:
        midle = (left + right) // 2
        if arr[midle] == element:
            return midle
        elif arr[midle] < element:
            left = midle + 1
        else:
            right = midle - 1
    return -1

find_number = int(input("Введите число для поиска: "))
if binary_serch(numbers, find_number) != -1:
    print(f"Элемент {find_number} найден в списке")
