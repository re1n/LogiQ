def draw_classroom(canvas, students):
	x_pos = 100
	y_pos = 200
	for student in students:
		canvas.create_oval(x_pos, y_pos, x_pos+50, y_pos+50, fill="white")
		item_list = ""
		if student["hasPencil"]:
			item_list += "P"
		if student["hasCalculator"]:
			item_list += "C"
		if student["hasLaptop"]:
			item_list += "L"
		canvas.create_text(x_pos, y_pos+60, text=item_list)
		x_pos += 100
