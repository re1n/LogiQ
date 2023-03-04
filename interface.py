import json
import tkinter as tk
from tkinter import ttk
from draw import draw_classroom, draw_sports, draw_pets
from generate import generate_classroom, generate_favourite_sports, generate_pets
from time import sleep

score = 0
q_count = 0
WIDTH = 1200
HEIGHT = 900
PADDING = 10
def check(vars, sentencePairs, canvas, base, ops, difficulty):
	global score, q_count, WIDTH, HEIGHT
	q_count += 1
	correct = True
	for i in range(0, 4):
		# Marked as true but is false
		if (vars[i].get() == 1) and (sentencePairs[i][1] == False):
			correct = False
		# Marked as false but is true
		if (vars[i].get() == 0) and (sentencePairs[i][1] == True):
			correct = False
	# Display correct/incorrect message
	canvas.create_rectangle(WIDTH/2-200, HEIGHT/3-100, WIDTH/2+200, HEIGHT/3+100, fill="green" if correct else "red")
	canvas.create_text(WIDTH/2, HEIGHT/3, text="Correct!" if correct else "Incorrect!", font=("Arial", 40), fill="white")
	score += 1 if correct else 0
	canvas.update()
	sleep(1)
	canvas.delete("all")
	if q_count == 5:
		f = open("usr.bin", "rb")
		user_list = list(f.read())
		points = user_list[7]
		if difficulty == 0:
			points += score
			user_list[0] += score
			user_list[1] += 5
		elif difficulty == 1:
			points += score*3
			user_list[2] += score
			user_list[3] += 5
		elif difficulty == 2:
			points += score*5
			user_list[4] += score
			user_list[5] += 5
		if points >= 25 and user_list[6] < 9:
			user_list[7] = points-25
			user_list[6] += 1
		else:
			user_list[7] = points
		f.close()
		f = open("usr.bin", "wb")
		f.write(bytearray(user_list))
		f.close()
		canvas.create_text(WIDTH/2, HEIGHT*0.3, text="You got " + str(score) + " out of 5 correct!", font=("Arial", 40), fill="green")
		canvas.update()
		sleep(3)
		score = 0
		q_count = 0
		menu(base)
	else:
		render(base, canvas, vars, ops, difficulty)

def render(base, canvas, vars, ops, difficulty):
	if difficulty == 0:
		sentences, objects = generate_classroom()
		draw_classroom(canvas, objects)
	elif difficulty == 1:
		sentences, objects = generate_favourite_sports()
		draw_sports(canvas, objects)
	else:
		sentences, objects = generate_pets()
		draw_pets(canvas, objects)
	for i in range(0, 4):
		ops[i].config(text=sentences[i][0], font=("Arial", 12))
		vars[i].set(0)
	ops[4].config(command=lambda : check(vars, sentences, canvas, base, ops, difficulty))
	base.update()

def setup_quiz(base, difficulty):
	global WIDTH, HEIGHT, PADDING
	for w in base.winfo_children():
		w.destroy()

	canvas = tk.Canvas(base)
	canvas.config(width=WIDTH, height=HEIGHT*0.6, bg="white")
	canvas.pack()

	var1, var2, var3, var4 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
	op1 = tk.Checkbutton(base, variable=var1)
	op1.place(x=PADDING, y=(HEIGHT*0.6)+PADDING, width=(WIDTH*0.5)-2*PADDING, height=(HEIGHT*0.2)-2*PADDING)
	op2 = tk.Checkbutton(base, variable=var2)
	op2.place(x=(WIDTH*0.5)+PADDING, y=(HEIGHT*0.6)+PADDING, width=(WIDTH*0.5)-2*PADDING, height=(HEIGHT*0.2)-2*PADDING)
	op3 = tk.Checkbutton(base, variable=var3)
	op3.place(x=PADDING, y=(HEIGHT*0.8)+PADDING, width=(WIDTH*0.5)-2*PADDING, height=(HEIGHT*0.2)-2*PADDING)
	op4 = tk.Checkbutton(base, variable=var4)
	op4.place(x=(WIDTH*0.5)+PADDING, y=(HEIGHT*0.8)+PADDING, width=(WIDTH*0.5)-2*PADDING, height=(HEIGHT*0.2)-2*PADDING)
	op5 = tk.Button(base, text="Submit")
	op5.place(x=(WIDTH*0.5)-50, y=(HEIGHT*0.8)-30, width=100, height=60)
	vars = [var1, var2, var3, var4]
	ops = [op1, op2, op3, op4, op5]

	render(base, canvas, vars, ops, difficulty)

def display_difficulties(base, start):
	start.destroy()
	easy = tk.Button(base, text="Easy", font=("Arial", 20), command=lambda : setup_quiz(base, 0))
	easy.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)-30, width=300, height=60)
	medium = tk.Button(base, text="Medium", font=("Arial", 20), command=lambda : setup_quiz(base, 1))
	medium.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)+60, width=300, height=60)
	hard = tk.Button(base, text="Hard", font=("Arial", 20), command=lambda : setup_quiz(base, 2))
	hard.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)+150, width=300, height=60)


def get_rank_names():
	f = open("usr.bin", "rb")
	user_list = list(f.read())
	f.close()
	f = open("ranks.json")
	ranks = json.load(f)
	f.close()
	rank_num = user_list[6]
	for i in range(0, len(ranks)):
		if ranks[i]["num"] == rank_num:
			return ranks[i]["name"], ranks[i+1]["name"]
	

def user_profile(base):
	for w in base.winfo_children():
		w.destroy()
	f = open("usr.bin", "rb")
	user_list = list(f.read())
	f.close()
	title = tk.Label(base, text="User Profile", font=("Arial", 40, "bold"))
	current, next = get_rank_names()
	rank = tk.Label(base, text="Current rank: " + current, font=("Arial", 30))
	title.place(x=0, y=0, width=WIDTH, height=100)
	rank.place(x=0, y=100, width=WIDTH, height=100)
	home = tk.Button(base, text="Home", font=("Arial", 20), command=lambda : menu(base))
	home.place(x=10, y=10, width=200, height=60)
	whole_bar = ttk.Progressbar(base, orient="horizontal", mode="determinate")
	whole_bar.place(x=(WIDTH/2)-250, y=(HEIGHT/2)-25, width=500, height=30)
	whole_bar["value"] = user_list[7]*4
	# write current end underneath left end of bar and next end underneath right end of bar
	cur_rank = tk.Label(base, text=current, font=("Arial", 20))
	cur_rank.place(x=(WIDTH/2)-350, y=(HEIGHT/2)+20, width=250, height=30)
	next_rank = tk.Label(base, text=next, font=("Arial", 20))
	next_rank.place(x=(WIDTH/2)+100, y=(HEIGHT/2)+20, width=250, height=30)
	success_rate = tk.Label(base, text="Success rates", font=("Arial", 30))
	success_rate.place(x=0, y=(HEIGHT/2)+100, width=WIDTH, height=40)
	easy = int(user_list[0]/user_list[1]*100) if user_list[1] != 0 else 0
	medium = int(user_list[2]/user_list[3]*100) if user_list[3] != 0 else 0
	hard = int(user_list[4]/user_list[5]*100) if user_list[5] != 0 else 0
	easy_rate = tk.Label(base, text="Easy: " + str(easy) + "%", font=("Arial", 20))
	easy_rate.place(x=0, y=(HEIGHT/2)+200, width=WIDTH, height=40)
	medium_rate = tk.Label(base, text="Medium: " + str(medium) + "%", font=("Arial", 20))
	medium_rate.place(x=0, y=(HEIGHT/2)+240, width=WIDTH, height=40)
	hard_rate = tk.Label(base, text="Hard: " + str(hard) + "%", font=("Arial", 20))
	hard_rate.place(x=0, y=(HEIGHT/2)+280, width=WIDTH, height=40)


def menu(base):
	# Clear screen
	for w in base.winfo_children():
		w.destroy()

	title = tk.Label(base, text="LogiQ", font=("Arial", 40, "bold"))
	title.place(x=0, y=0, width=WIDTH, height=100)

	start = tk.Button(base, text="Start", font=("Arial", 20), command=lambda : display_difficulties(base, start))
	start.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)-30, width=300, height=60)

	profile = tk.Button(base, text="Profile", font=("Arial", 20), command=lambda : user_profile(base))
	profile.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)+60, width=300, height=60)


def setup():
	global WIDTH, HEIGHT
	base = tk.Tk()
	base.title("LogiQ")
	base.geometry(f"{WIDTH}x{HEIGHT}")

	menu(base)

	base.mainloop()

setup()
