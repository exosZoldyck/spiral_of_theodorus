# Spiral of Theodorus (1.0) by exosZoldyck

import turtle
import math

turtle.speed(0)
turtle.hideturtle()

print("Set minumum lenght unit:")
minLenght = int(input())
print("To which square root should the program draw?")
sqrtLimit = int(input())

turtle.bk(minLenght)
turtle.lt(90)
turtle.fd(minLenght)
x = turtle.xcor()
y = turtle.ycor()
turtle.home()

x_new = x
y_new = y
turnAmount = 180 + 45
currentSqrt = 3
i = 2

while i < sqrtLimit:
    x = x_new
    y = y_new
    
    turnAmount += (math.degrees(math.asin(1/math.sqrt(currentSqrt))))
    turtle.rt(turnAmount)
    
    turtle.fd(math.sqrt(currentSqrt) * minLenght)
    x_new = turtle.xcor()
    y_new = turtle.ycor()
    turtle.goto(x,y)

    turtle.home()
    currentSqrt += 1
    i += 1


