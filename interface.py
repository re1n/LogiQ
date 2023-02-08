import tkinter as tk
from draw import draw_classroom
from logic import generate_classroom
from time import sleep

score = 0
q_count = 0
def check(vars, sentencePairs, canvas, base, ops):
	global score, q_count
	q_count += 1
	correct = True
	for i in range(0, 4):
		if (vars[i].get() == 1) and (sentencePairs[i][1] == False):
			correct = False
		if (vars[i].get() == 0) and (sentencePairs[i][1] == True):
			correct = False
	canvas.create_text(400, 350, text="Correct!" if correct else "Incorrect!", font=("Arial", 30), fill="green" if correct else "red")
	score += 1 if correct else 0
	canvas.update()
	sleep(1)
	canvas.delete("all")
	if q_count == 5:
		canvas.create_text(400, 350, text="You got " + str(score) + " out of 5 correct!", font=("Arial", 30), fill="green")
		canvas.update()
		sleep(3)
		base.destroy()
		return
	render(base, canvas, vars, ops)

def render(base, canvas, vars, ops):
	classroomPairs, students = generate_classroom()
	for i in range(0, 4):
		ops[i].config(text=classroomPairs[i][0], font=("Arial", 12))
		vars[i].set(0)
	ops[4].config(command=lambda : check(vars, classroomPairs, canvas, base, ops))
	base.update()
	draw_classroom(canvas, students)

def setup():
	base = tk.Tk()
	base.title("LogiQ")
	base.geometry("800x640")

	canvas = tk.Canvas(base)
	canvas.config(width=800, height=400, bg="white")
	canvas.pack()

	var1, var2, var3, var4 = tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()
	op1 = tk.Checkbutton(base, variable=var1)
	op1.place(x=10, y=410, width=380, height=100)
	op2 = tk.Checkbutton(base, variable=var2)
	op2.place(x=410, y=410, width=380, height=100)
	op3 = tk.Checkbutton(base, variable=var3)
	op3.place(x=10, y=530, width=380, height=100)
	op4 = tk.Checkbutton(base, variable=var4)
	op4.place(x=410, y=530, width=380, height=100)
	op5 = tk.Button(base, text="Submit")
	op5.place(x=360, y=480, width=100, height=60)
	vars = [var1, var2, var3, var4]
	ops = [op1, op2, op3, op4, op5]

	render(base, canvas, vars, ops)

	base.mainloop()

setup()