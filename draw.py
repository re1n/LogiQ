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
