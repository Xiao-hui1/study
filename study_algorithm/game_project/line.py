import turtle as t
t.pensize(1)
t.bgcolor('black')
i = 1
while i <= 100:
    if i % 4 == 0:
        t.color('red')
    if i % 4 == 1:
        t.color('yellow')
    if i % 4 == 2:
        t.color('purple')
    if i % 4 == 3:
        t.color('blue')
    t.forward(2*i)
    t.left(91)
    i += 1