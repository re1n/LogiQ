import random
from math import ceil
from logic import generateShapes, generateNumShapes

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
	
def generateBoxList(canvas):
	boxes = []
	x, y = 0, 0
	for i in range(3):
		for j in range(4):
			boxes.append([x+10, y+10, x + round(canvas.winfo_width() / 4)-10, y + round(canvas.winfo_height() / 3)-10])
			x += round(canvas.winfo_width() / 4)
		x = 0
		y += round(canvas.winfo_height() / 3)
			
	return boxes

def draw_shapes(canvas):
	num_shapes = 6
	shapes = generateNumShapes(num_shapes)
	boxes = generateBoxList(canvas)

	for pair in shapes:
		shape = pair[0]
		colour = pair[1]
		box = random.choice(boxes)
		boxes.remove(box)
		if shape == "triangle":
			height = box[3] - box[1]
			length = box[2] - box[0]
			diff = (length-height)/2
			midpoint = (box[0] + box[2]) / 2
			canvas.create_polygon(box[2]-diff-height, box[3], midpoint, box[1], box[2]-diff, box[3], fill=colour, outline="black")
		elif shape == "square":
			height = box[3] - box[1]
			length = box[2] - box[0]
			diff = (length-height)/2
			canvas.create_rectangle(box[0] + diff, box[1], box[2] - diff, box[3], fill=colour)