import random

def generateSentence(mainSentence):
	# Generate a first order logic sentence
	shapes = ["triangle", "square", "circle"]
	colours = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "cyan"]
	quantifiers = ["∀", "∃"]
	operators = ["⇒", "⇔"]
	shape = random.choice(shapes)
	colour = random.choice(colours)
	quantifier = random.choice(quantifiers)
	operator = random.choice(operators)
	sentence = quantifier + "x(" + shape + "(x) " + operator + " " + colour + "(x))"
	if mainSentence is True:
		return sentence, shape, colour, operator, quantifier
	else:
		return sentence

def generateShapes(shape, colour, operator, quantifier):
	shapes = ["triangle", "square", "circle"]
	colours = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "cyan"]
	picked_shapes_and_colours = [[shape, colour]]
	for i in range(0,3):
		chosen_shape = random.choice(shapes)
		chosen_colour = random.choice(colours)
		picked_shapes_and_colours.append([chosen_shape, chosen_colour])

	if operator == "⇒":
		if quantifier == "∀":
			for i in range(1,4):
				if picked_shapes_and_colours[i][0] == shape and picked_shapes_and_colours[i][1] != colour:
					picked_shapes_and_colours[i][1] = colour
	elif operator == "⇔":
		if quantifier == "∀":
			for i in range(1,4):
				if picked_shapes_and_colours[i][0] == shape:
					picked_shapes_and_colours[i][1] = colour
				if picked_shapes_and_colours[i][1] == colour:
					picked_shapes_and_colours[i][0] = shape
	random.shuffle(picked_shapes_and_colours)
	return picked_shapes_and_colours

def generateNumShapes(num):
	shapes = ["triangle", "square", "circle"]# "diamond", "hexagon"]
	colours = ["red", "green", "blue", "purple", "orange", "yellow", "pink", "cyan"]
	picked_shapes_and_colours = []
	for i in range(0, num):
		chosen_shape = random.choice(shapes)
		chosen_colour = random.choice(colours)
		picked_shapes_and_colours.append([chosen_shape, chosen_colour])
	return picked_shapes_and_colours