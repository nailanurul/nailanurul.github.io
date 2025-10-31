from turtle import *

getscreen()
bgcolor("light blue")

speed(1)

penup()
forward(100)
pendown()

fillcolor("white")
begin_fill()

for i in range(3):
    forward(200)
    left(360/3)

    shape("turtle")

end_fill()

done()