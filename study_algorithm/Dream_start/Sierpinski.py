import turtle
def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

def getMid(point,points):
    return ((point[0]+points[0]) / 2,(point[1]+points[1]) / 2)

def sierpinski(degree,points):
    colormap = ["blue","red","green","white","yellow","orange"]
    drawTriangle(points,colormap[degree])
    if degree > 0:
        sierpinski(degree-1,
                   {'left':points['left'],
                    'top':getMid(points['left'],points['top']),
                    'right':getMid(points['left'],points['right'])})

        sierpinski(degree - 1,
                   {'left': getMid(points['left'],points['top']),
                    'top':  points['top'],
                    'right': getMid(points['top'], points['right'])})
        sierpinski(degree - 1,
                   {'left': getMid(points['left'],points['right']),
                    'top': getMid(points['top'], points['right']),
                    'right': points['right']})

t = turtle.Turtle()

points = {'left':(-200,-100),
          'top':(0,200),
          'right':(200,-100)}
sierpinski(5,points)

turtle.done()
