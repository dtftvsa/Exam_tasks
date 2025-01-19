def func(x, y):
    if x == y:
        return 1
    elif x > y or x == 15:
        return 0
    else:
        return func(x + 1, y) + func(x + 2, y)
print(func(3, 9) * func(9, 20))