# import random
# s = [random.randint(-10, 10) for i in range(10)]
#
# print(s)
# # print(sorted(s, reverse=True))
# print(sorted(s, key = pow))

##################################

# student = [
#     ('jon', 'A', 15),
#     ('asdas', 'B', 15),
#     ('afsfas', 'B', 15),
# ]
#
# sorted_std = sorted(student, key=lambda st: st[2], reverse=True)
# print(sorted_std)

################################## 6
# Напишите программу, которая сортирует список словарей по значениям
# ключей, которые являются списками, по сумме элементов в этих списках, с
# использованием функции sorted() и выводит отсортированный список.

# s = [
#     {'a': 2, 'b': 2, 'c': 3},
#     {'d': 4, 'e': 5, 'f': 6},
# ]
#
# t = sorted(s, key=lambda ss: ss[0])
#
# print(t)

# фильтр фильтрует список по условию

# Filter( )
################################# 10. Напишите программу, которая фильтрует слова из списка по их длине
# (например, длина больше 5 символов).

# s = ['asd', 'asdasd', 'aasd']
# d = list(filter(lambda x: len(x) > 5, s))
# print(d)

############################## 11
# Напишите программу, которая фильтрует студентов по их оценкам (например, выше среднего).

# std = [
#     {'name': 'alex1', 'grade': 42},
#     {'name': 'alex1', 'grade': 45},
#     {'name': 'alex1', 'grade': 23},
#     {'name': 'alex1', 'grade': 56},
# ]
#
# avg_grade = sum(i['grade'] for i in std) / len(std)
#
# f = list(filter(lambda std: std['grade'] > avg_grade, std))
#
# print(f)

############################### 12
# Напишите программу, которая фильтрует слова из списка, начинающиеся с определенной буквы

# s = ['Asdf', 'Bnm', 'Cdsdf', 'kasd']
#
# d = list(filter(lambda t: t.lower().startswith('a'), s))
#
# print(d)