############################################### 1
# Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое
# всех элементов больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить
# в обратном порядке.

# list_1 = [6, 2, 5, 3, 1, 9, 8, -10, -3]
# copy_list_1 = list_1.copy()
# sr_ar_list_1 = sum(list_1) / len(list_1)
# new_list_1 = []
# if sr_ar_list_1 > 0:
#     for i in range(round(len(list_1) * 2 / 3)):
#         new_list_1.append(list_1[i])
#         copy_list_1.remove(list_1[i])
#     print(f"Среднее арифметическое = {sr_ar_list_1}")
#     print(sorted(new_list_1) + sorted(copy_list_1, reverse=True))
# else:
#     for i in range(0, round(len(list_1) / 3)):
#         new_list_1.append(list_1[i])
#         copy_list_1.remove(list_1[i])
#     print(f"Среднее арифметическое = {sr_ar_list_1}")
#     print(sorted(new_list_1) + sorted(copy_list_1, reverse=True))

############################################### 2
# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию


# def input_of_ratings(grade):
#     i = 0
#     while i < 10:
#         a = int(input("Введите 10 оценок (балл от 1 до 12): "))
#         grade.append(a)
#         i += 1
#         if i < 10:
#             print(f"*** Осталось ввести: {10 - i} ***")
#     return grade
#
#
# def output_of_ratings(grade):
#     if not grade:
#         print("*** Оценок ещё не вносили! ***\n")
#         print()
#         return
#     for i in range(len(grade)):
#         print(f"№{i + 1} - {grade[i]}")
#         print()
#     return
#
#
# def change_the_rating(grade):
#     if not grade:
#         print("*** Оценок ещё не вносили! ***\n")
#         print()
#         return
#     n = int(input("Введите номер оценки, которую хотите поменять: "))
#     n_grade = int(input("Введите оценку: "))
#     for i in range(len(grade)):
#         if n == i + 1:
#             grade[i] = n_grade
#             print(f"Оценка {grade[i]} успешно заменена на {n_grade}!!!")
#             print()
#
#
# def stipend(grade):
#     if not grade:
#         print("*** Оценок ещё не вносили! ***\n")
#         print()
#         return
#     sr_bal = sum(grade) / len(grade)
#     if sr_bal >= 10.7:
#         print(f"Средний бал: {sr_bal} Поздравляю! Вам положена стипендия!!!")
#         print()
#     else:
#         print(f"Средний бал: {sr_bal} - Стипендии не будет!!!")
#         print()
#
#
# def list_up(grade):
#     if not grade:
#         print("*** Оценок ещё не вносили! ***\n")
#         print()
#         return
#     print(sorted(grade))
#
#
# def list_down(grade):
#     if not grade:
#         print("*** Оценок ещё не вносили! ***\n")
#         print()
#         return
#     print(sorted(grade, reverse=True))
#
#
# def main():
#
#     grade = []
#     while True:
#         answer = input(f"Mеню:\n"
#                        f"1 - Ввод оценок\n"
#                        f"2 - Вывод оценок (вывод содержимого списка)\n"
#                        f"3 - Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку)\n"
#                        f"4 - Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7)\n"
#                        f"5 - Вывод отсортированного списка оценок: по возрастанию\n"
#                        f"6 - Вывод отсортированного списка оценок: по убыванию\n"
#                        f"0 - Выход\n")
#         if answer == "1":
#             input_of_ratings(grade)
#         elif answer == "2":
#             output_of_ratings(grade)
#         elif answer == "3":
#             change_the_rating(grade)
#         elif answer == "4":
#             stipend(grade)
#         elif answer == "5":
#             list_up(grade)
#         elif answer == "6":
#             list_down(grade)
#         elif answer == "0":
#             print("*** Выход из программы ***")
#             break
#         else:
#             print("*** Неверные данные ***")
#             print()
#
#
# main()


