count = 0
for a in range(1000, 0, -1):
    k = 0
    for x in range(0, 500):
        for y in range(0, 500):
            if (y + 2 * x != 48) or (a < x) or (a < y):
                k += 1
    if k == 250000:
        print(a)
        break