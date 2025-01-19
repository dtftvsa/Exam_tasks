def func(x, y):
    if x == y:
        return 1
    elif x < y:
        return 0
    else:
        return func(x - 2, y) + func(x // 2, y)
print(func(38, 16) * func(16, 2))