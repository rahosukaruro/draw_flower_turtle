import turtle

# Definitions

def draw_square():
	# Create instance of Turtle and name it carturtle
	carturtle = turtle.Turtle()
	carturtle.shape("turtle")
	carturtle.color("green")
	carturtle.speed(1)

	i = 0
	while i < 4:
		# Move carturtle
		carturtle.forward(100)
		# Turn carturtle Right by 90 degrees
		carturtle.right(90)

		i += 1


def draw_circle():
	# Create instance of Turtle and name it annturtle
	annturtle = turtle.Turtle()
	annturtle.shape("turtle")
	annturtle.color("pink")
	annturtle.circle(50)


def draw_triangle():
	# Create instance of Turtle and name it yuanturtle
	yuanturtle = turtle.Turtle()
	yuanturtle.shape("turtle")
	yuanturtle.color("orange")
	yuanturtle.right(120)

	i = 0
	while i < 3:
		# Move carturtle
		yuanturtle.forward(110)
		# Turn carturtle Right by 90 degrees
		yuanturtle.right(120)

		i += 1


def draw_square_circle_art():
	# Create instance of Turtle and name it lunaturtle
	lunaturtle = turtle.Turtle()
	lunaturtle.shape("turtle")
	lunaturtle.color("blue")
	lunaturtle.speed(0)

	# Iterate 10 times to make square
	i = 0 
	while i < 75:
		lunaturtle.right(5)

		# Draw big Square
		j = 0 
		while j < 4:
			# Move carturtle
			lunaturtle.forward(150)
			# Turn carturtle Right by 90 degrees
			lunaturtle.right(90)

			j += 1

		i += 1

	lunaturtle.right(75)
	lunaturtle.forward(300)


# Main Process
window = turtle.Screen()
window.bgcolor("white")

#draw_square()
#draw_circle()
#draw_triangle()
draw_square_circle_art()

window.exitonclick()