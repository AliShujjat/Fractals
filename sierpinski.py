import turtle
jeff = turtle.Turtle()
jeff.speed(50)
def sierpinski(length,level):
  if level == 0:
    for i in range(3):
      jeff.forward(length)
      jeff.lt(120)
  else:
    sierpinski(length/2,level-1)
    jeff.fd(length/2)
    sierpinski(length/2,level-1)
    jeff.lt(120)
    jeff.fd(length/2)
    jeff.rt(120)
    sierpinski(length/2,level-1)
    jeff.rt(120)
    jeff.fd(length/2)
    jeff.lt(120)

sierpinski(200,5)