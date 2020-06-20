import turtle
jeff = turtle.Turtle()
jeff.speed(50)
def koch_curve(length, level):
  if level == 0:
    jeff.fd(length)
  else:
      koch_curve(length/3, level-1)
      jeff.rt(60)
      koch_curve(length/3, level-1)
      jeff.lt(120)
      koch_curve(length/3, level-1)
      jeff.rt(60)
      koch_curve(length/3, level-1)

def koch_snowflake(length,level):
  for i in range(6):
    koch_curve(length,level)
    jeff.rt(60)

