import turtle
""" Draw a flower in Python"""

def draw_square(square):
	for i in range(0,2):
		square.forward(100)
		square.right(30)
		square.forward(100)
		square.right(150)


def draw_flower():
	window = turtle.Screen()
	window.bgcolor("green")

	pen = turtle.Turtle()
	pen.shape("triangle")
	pen.color("#99FF00")

	for i in range(0,36):
		draw_square(pen)
		pen.right(10)

	for i in range(0,4):
		pen.circle(50)
		pen.right(90)
	pen.right(90)
	pen.forward(300)
	pen.right(90)
	draw_square(pen)
	pen.left(180)
	draw_square(pen)
	pen.left(270)
	pen.forward(200)

	window.exitonclick()

draw_flower()