def draw_classroom(canvas, students):
	y_pos = 150
	# Evenly space the students with a 50px buffer
	num_students = len(students)
	circle_size = 70
	circle_spacing = 50
	x_pos = (1200 - circle_size * num_students - circle_spacing * (num_students-1)) / 2
	for student in students:
		# Draw the student's circle
		canvas.create_oval(x_pos, y_pos, x_pos+circle_size, y_pos+circle_size, fill="white", outline="black", width=3)
		# Draw the student's items
		item_list = ""
		if student["hasCalculator"]:
			item_list += "C"
		if student["hasLaptop"]:
			item_list += "L"
		if student["hasPencil"]:
			item_list += "P"
		# Draw the student's items centered in the circle
		canvas.create_text(x_pos + circle_size/2, y_pos + circle_size/2, text=item_list, font=("Arial", 20))
		x_pos += circle_size + circle_spacing

	# Clarify domain
	canvas.create_text(400, 350, text="Each circle represents a student.\nThe domain of 'x' consists of students in the image.", font=("Arial", 15), justify="center")

	# Key
	canvas.create_rectangle(10, 10, 200, 105, fill="#f5f5f5", outline="")

	canvas.create_text(15, 15, text="C = Has a calculator", font=("Arial", 15), anchor="nw")
	canvas.create_text(15, 45, text="L = Has a laptop", font=("Arial", 15), anchor="nw")
	canvas.create_text(15, 75, text="P = Has a pencil", font=("Arial", 15), anchor="nw")

def draw_sports(canvas, people):
	# Evenly space the people with a 50px buffer
	num_people = len(people)
	circle_size = 70
	circle_spacing = 75
	x_pos = (1200 - circle_size * num_people - circle_spacing * (num_people-1)) / 2
	for person in people:
		y_pos = 100
		# Draw the person's circle
		canvas.create_oval(x_pos, y_pos, x_pos+circle_size, y_pos+circle_size, fill="white", outline="black", width=3)
		y_pos += circle_size + 20
		# Write "likes" under the person's circle
		canvas.create_text(x_pos + circle_size/2, y_pos, text="Likes:", font=("Arial", 15))
		y_pos += 20
		if not person["likes"]:
			canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
			y_pos += 20
		for like in person["likes"]:
			# Draw the person's likes
			canvas.create_text(x_pos + circle_size/2, y_pos, text=f"• {like.capitalize()}", font=("Arial", 15))
			y_pos += 20
		y_pos += 20
		canvas.create_text(x_pos + circle_size/2, y_pos, text="Dislikes:", font=("Arial", 15))
		y_pos += 20
		if not person["dislikes"]:
			canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
			y_pos += 20
		for dislike in person["dislikes"]:
			# Draw the person's dislikes
			canvas.create_text(x_pos + circle_size/2, y_pos, text=f"• {dislike.capitalize()}", font=("Arial", 15))
			y_pos += 20
		x_pos += circle_size + circle_spacing
