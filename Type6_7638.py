from turtle import *
tracer(0)
left(90)
k = 20
for _ in range(9):
    forward(12 * k)
    right(90)
    forward(6 * k)
    right(90)

pu()
forward(k)
right(90)
forward(3 * k)
left(90)

pd()
for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)

pu()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x * k, y * k)
        dot(5)
done()