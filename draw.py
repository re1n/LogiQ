import random
from logic import generateShapes

def shapes(canvas, main_sentence):
	shapes_and_colours = generateShapes(main_sentence[1], main_sentence[2], main_sentence[3], main_sentence[4])
	# Draw one shape in each quarter of the canvas

	# Top left
	if shapes_and_colours[0][0] == "triangle":
		canvas.create_polygon(100, 150, 150, 50, 200, 150, fill=shapes_and_colours[0][1], outline="black")
	elif shapes_and_colours[0][0] == "square":
		canvas.create_rectangle(100, 50, 200, 150, fill=shapes_and_colours[0][1])
	elif shapes_and_colours[0][0] == "circle":
		canvas.create_oval(100, 50, 200, 150, fill=shapes_and_colours[0][1])
	# Top right
	if shapes_and_colours[1][0] == "triangle":
		canvas.create_polygon(600, 150, 650, 50, 700, 150, fill=shapes_and_colours[1][1], outline="black")
	elif shapes_and_colours[1][0] == "square":
		canvas.create_rectangle(600, 50, 700, 150, fill=shapes_and_colours[1][1])
	elif shapes_and_colours[1][0] == "circle":
		canvas.create_oval(600, 50, 700, 150, fill=shapes_and_colours[1][1])
	# Bottom left
	if shapes_and_colours[2][0] == "triangle":
		canvas.create_polygon(100, 350, 150, 250, 200, 350, fill=shapes_and_colours[2][1], outline="black")
	elif shapes_and_colours[2][0] == "square":
		canvas.create_rectangle(100, 250, 200, 350, fill=shapes_and_colours[2][1])
	elif shapes_and_colours[2][0] == "circle":
		canvas.create_oval(100, 250, 200, 350, fill=shapes_and_colours[2][1])
	# Bottom right
	if shapes_and_colours[3][0] == "triangle":
		canvas.create_polygon(600, 350, 650, 250, 700, 350, fill=shapes_and_colours[3][1], outline="black")
	elif shapes_and_colours[3][0] == "square":
		canvas.create_rectangle(600, 250, 700, 350, fill=shapes_and_colours[3][1])
	elif shapes_and_colours[3][0] == "circle":
		canvas.create_oval(600, 250, 700, 350, fill=shapes_and_colours[3][1])
	