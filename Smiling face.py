import turtle

screen = turtle.Screen()
screen.title("Detailed Smiley Face Drawing")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)  
pen.width(3)  

def draw_circle(radius, color, x, y):
    pen.penup()
    pen.goto(x, y - radius)  
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius) 
    pen.end_fill()

def draw_line(x1, y1, x2, y2, width=3, color="black"):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.width(width)
    pen.color(color)
    pen.goto(x2, y2)

draw_circle(100, "yellow", 0, 0)

draw_circle(15, "black", -35, 35)

draw_circle(15, "black", 35, 35)

draw_circle(10, "black", 0, 15)

draw_line(-55, 60, -15, 70, width=5, color="black")
draw_line(15, 70, 55, 60, width=5, color="black")

pen.penup()
pen.goto(-50, -10)  
pen.pendown()
pen.setheading(-60)  
pen.circle(50, 120)  

hair_positions = [
    (-70, 110), (-50, 130), (-30, 140), (0, 150), (30, 140), (50, 130), (70, 110)
]
for pos in hair_positions:
    pen.penup()
    pen.goto(pos)  
    pen.pendown()
    pen.setheading(90)  
    pen.forward(30)  

pen.hideturtle()

screen.mainloop()
