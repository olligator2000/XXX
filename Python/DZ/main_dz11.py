############################################### 1
# Написать рекурсивную функцию нахождения наибольшего общего делителя двух целых чисел.
def nod(a, b):
    if a == b:
        return a
    elif a > b:
        return nod(a - b, b)
    else:
        return nod(a, b - a)


print(nod(22, 16))
