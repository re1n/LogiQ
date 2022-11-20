import random

def shapes(canvas):
	# Assume canvas is 800x400
	shapes = ["triangle", "square", "circle"]
	colours = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "cyan"]
	# Draw a blue triangle in the first quadrant
	canvas.create_polygon(100, 100, 200, 100, 150, 200, fill="blue", outline="")
	for i in range(1,4):
		shape = random.choice(shapes)
		colour = random.choice(colours)
		if shape == "triangle":
			canvas.create_polygon(200 * i + 100, 200, 200 * i + 200, 200, 200 * i + 150, 100, fill="blue", outline="")
		elif shape == "square":
			canvas.create_rectangle(200 * i + 100, 100, 200 * i + 200, 200, fill=colour, outline="")
		elif shape == "circle":
			canvas.create_oval(200 * i + 100, 100, 200 * i + 200, 200, fill=colour, outline="")