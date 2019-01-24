# coding:utf-8(低版本适用)

import turtle

turtle.screensize(400, 400)

# 正方形
turtle.penup()
turtle.goto(-350, 250)
turtle.pendown()
turtle.pencolor('green')
turtle.begin_fill()
turtle.fillcolor('green')
for i in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()

# 矩形
turtle.penup()
turtle.goto(-200, 250)
turtle.pendown()
turtle.pencolor('blue')
turtle.begin_fill()
turtle.fillcolor('blue')
for i in range(1, 5):
    if i % 2 == 1:
        n = 120
    elif i % 2 == 0:
        n = 80
    turtle.forward(n)
    turtle.left(90)

turtle.end_fill()
turtle.penup()

# 正方体
x = 0
y = 200
n = 80
turtle.goto(x, y)
turtle.pendown()
turtle.pencolor('black')
turtle.begin_fill()
turtle.fillcolor('black')
for i in range(4):
    turtle.forward(n)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(x, y + n)
turtle.pendown()
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.left(45)
turtle.forward(int(n * 0.6))  # 上方左侧斜线
turtle.right(45)
turtle.forward(n)  # 上方横线
turtle.left(360 - 135)
turtle.forward(int(n * 0.6))  # 上方右侧斜线
turtle.end_fill()

turtle.left(45)
turtle.penup()
turtle.goto(x + n, y)

turtle.pendown()
turtle.left(135)
turtle.forward(int(n * 0.6))
turtle.left(45)
turtle.forward(n)
turtle.right(90)  # 方向还原，向左
turtle.penup()

# 五角星
turtle.goto(x + 200, y)
turtle.pendown()
turtle.pencolor('orange')
turtle.begin_fill()
turtle.fillcolor('orange')
turtle.left(36)
for i in range(5):
    turtle.forward(120)
    turtle.left(180 - 36)
turtle.end_fill()
turtle.right(36)
turtle.penup()

# -----------------------------------------------------
# 奥运五环

x = -300
y = 50
r = 60
# 第一个圈，蓝色
turtle.goto(x, y)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('blue')
turtle.circle(r)
turtle.penup()

# 第二个圈，黑色
turtle.goto(x + 2.5 * r, y)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('black')
turtle.circle(r)
turtle.penup()

# 第三个圈，红色
turtle.goto(x + 2.5 * r * 2, y)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('red')
turtle.circle(r)
turtle.penup()

# 第四个圈，黄色
turtle.goto(x + (2.5 * r) * 0.5, y - r)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('yellow')
turtle.circle(r)
turtle.penup()

# 第五个圈，绿色
turtle.goto(x + (2.5 * r) * 0.5 + 2.5 * r, y - r)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor('green')
turtle.circle(r)
turtle.penup()

turtle.done()