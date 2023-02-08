from PIL import Image, ImageTk
import torch
import torchvision
import torchvision.transforms.functional as TF

def draw_pets(canvas, sprites):
	global man, woman, dog, dog_r, dog_g, dog_b, cat, cat_r, cat_g, cat_b
	man = Image.open("sprites/man.png")
	woman = Image.open("sprites/woman.png")
	ar_man = float(man.size[0]) / float(man.size[1])
	ar_woman = float(woman.size[0]) / float(woman.size[1])
	man = ImageTk.PhotoImage(man.resize((int(ar_man * 256), 256)))
	woman = ImageTk.PhotoImage(woman.resize((int(ar_woman * 256), 256)))
	dog = Image.open("sprites/dog.png")
	dog_a = dog.getchannel("A")
	ar_dog = float(dog.size[0]) / float(dog.size[1])
	dog_r = TF.adjust_hue(dog, -0.1)
	dog_r.putalpha(dog_a)
	dog_r = ImageTk.PhotoImage(dog_r.resize((int(ar_dog * 64), 64)))
	dog_g = TF.adjust_hue(dog, 0.2)
	dog_g.putalpha(dog_a)
	dog_g = ImageTk.PhotoImage(dog_g.resize((int(ar_dog * 64), 64)))
	dog_b = TF.adjust_hue(dog, 0.5)
	dog_b.putalpha(dog_a)
	dog_b = ImageTk.PhotoImage(dog_b.resize((int(ar_dog * 64), 64)))
	dog = ImageTk.PhotoImage(dog.resize((int(ar_dog * 64), 64)))
	cat = Image.open("sprites/cat.png")
	cat_a = cat.getchannel("A")
	ar_cat = float(cat.size[0]) / float(cat.size[1])
	cat_r = TF.adjust_hue(cat, -0.1)
	cat_r.putalpha(cat_a)
	cat_r = ImageTk.PhotoImage(cat_r.resize((int(ar_cat * 64), 64)))
	cat_g = TF.adjust_hue(cat, 0.2)
	cat_g.putalpha(cat_a)
	cat_g = ImageTk.PhotoImage(cat_g.resize((int(ar_cat * 64), 64)))
	cat_b = TF.adjust_hue(cat, 0.5)
	cat_b.putalpha(cat_a)
	cat_b = ImageTk.PhotoImage(cat_b.resize((int(ar_cat * 64), 64)))
	cat = ImageTk.PhotoImage(cat.resize((int(ar_cat * 64), 64)))


	pos_x = 100
	pos_y = 150
	for sprite in sprites:
		if sprite[0] == "Man":
			canvas.create_image(pos_x, pos_y, image=man)
		elif sprite[0] == "Woman":
			canvas.create_image(pos_x, pos_y, image=woman)
		if sprite[1] == "Dog":		
			if sprite[2] == "Red":
				canvas.create_image(pos_x, pos_y+150, image=dog_r)
			elif sprite[2] == "Blue":
				canvas.create_image(pos_x, pos_y+150, image=dog_b)
			elif sprite[2] == "Green":
				canvas.create_image(pos_x, pos_y+150, image=dog_g)
			else:
				canvas.create_image(pos_x, pos_y+150, image=dog)
		elif sprite[1] == "Cat":
			if sprite[2] == "Red":
				canvas.create_image(pos_x, pos_y+150, image=cat_r)
			elif sprite[2] == "Blue":
				canvas.create_image(pos_x, pos_y+150, image=cat_b)
			elif sprite[2] == "Green":
				canvas.create_image(pos_x, pos_y+150, image=cat_g)
			else:
				canvas.create_image(pos_x, pos_y+150, image=cat)
		pos_x += 150

def draw_classroom(canvas, students):
	# Student can have any combination of a pencil, calculator and laptop
	# Student is represented as a circle, there should be some small text below the circle
	# P for pencil, C for calculator, L for laptop
	# `students` is a list of dictionaries, each dictionary has the following keys:
	# "name": name of the student
	# "hasPencil": True if the student has a pencil, False otherwise
	# "hasCalculator": True if the student has a calculator, False otherwise
	# "hasLaptop": True if the student has a laptop, False otherwise
	# Canvas is 800x400px, students should not overlap

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
