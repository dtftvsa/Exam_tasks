count = 0
for a in range(0, 1000):
    k = 0
    for x in range(0, 500):
        for y in range(0, 500):
            if (y + 2 * x < a) or (x > 30) or (y > 20):
                k += 1
    if k == 250000:
        print(a)
        break
