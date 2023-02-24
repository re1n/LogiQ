import tkinter as tk
from draw import draw_classroom, draw_sports
from logic import generate_classroom, generate_favourite_sports
from time import sleep

score = 0
q_count = 0
WIDTH = 1200
HEIGHT = 900
PADDING = 10
def check(vars, sentencePairs, canvas, base, ops):
	global score, q_count, WIDTH, HEIGHT
	q_count += 1
	correct = True
	for i in range(0, 4):
		if (vars[i].get() == 1) and (sentencePairs[i][1] == False):
			correct = False
		if (vars[i].get() == 0) and (sentencePairs[i][1] == True):
			correct = False
	#canvas.create_text(WIDTH/2, HEIGHT*0.3, text="Correct!" if correct else "Incorrect!", font=("Arial", 40), fill="green" if correct else "red")
	# display correct in a green box with white text, incorrect in a red box with white text
	canvas.create_rectangle(WIDTH/2-200, HEIGHT/3-100, WIDTH/2+200, HEIGHT/3+100, fill="green" if correct else "red")
	canvas.create_text(WIDTH/2, HEIGHT/3, text="Correct!" if correct else "Incorrect!", font=("Arial", 40), fill="white")

	score += 1 if correct else 0
	canvas.update()
	sleep(1)
	canvas.delete("all")
	if q_count == 5:
		canvas.create_text(WIDTH/2, HEIGHT*0.3, text="You got " + str(score) + " out of 5 correct!", font=("Arial", 40), fill="green")
		canvas.update()
		sleep(3)
		score = 0
		q_count = 0
		menu(base)
	render(base, canvas, vars, ops)

def render(base, canvas, vars, ops):
	classroomPairs, students = generate_favourite_sports()
	for i in range(0, 4):
		ops[i].config(text=classroomPairs[i][0], font=("Arial", 12))
		vars[i].set(0)
	ops[4].config(command=lambda : check(vars, classroomPairs, canvas, base, ops))
	base.update()
	draw_sports(canvas, students)

def setup_quiz(base):
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
	# place submit button directly in the center of the four options
	op5.place(x=(WIDTH*0.5)-50, y=(HEIGHT*0.8)-30, width=100, height=60)
	vars = [var1, var2, var3, var4]
	ops = [op1, op2, op3, op4, op5]

	render(base, canvas, vars, ops)

def menu(base):
	for w in base.winfo_children():
		w.destroy()

	title = tk.Label(base, text="LogiQ", font=("Arial", 30))
	title.place(x=0, y=0, width=WIDTH, height=100)

	start = tk.Button(base, text="Start", font=("Arial", 20), command=lambda : setup_quiz(base))
	# place start button directly in the center of the screen
	start.place(x=(WIDTH*0.5)-150, y=(HEIGHT*0.5)-30, width=300, height=60)


def setup():
	global WIDTH, HEIGHT
	base = tk.Tk()
	base.title("LogiQ")
	base.geometry(f"{WIDTH}x{HEIGHT}")

	menu(base)

	base.mainloop()

setup()