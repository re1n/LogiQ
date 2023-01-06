from tkinter import Tk, Canvas, Checkbutton, Button, IntVar
from draw import draw_shapes
from logic import generateSentence
import random
from time import sleep

def check(vars, sentences, main_sentence, canvas):
	correct = True
	for i in range(0, 4):
		if vars[i].get() == 1:
			if sentences[i] != main_sentence:
				correct = False
	test = canvas.create_text(400, 200, text="Correct!" if correct else "Incorrect!", font=("Arial", 30))
	canvas.update()
	sleep(2)
	canvas.delete(test)

def setup():
	base = Tk()
	base.title("LogiQ")
	base.geometry("800x640")

	canvas = Canvas(base)
	canvas.config(width=800, height=400, bg="white")
	canvas.pack()

	main_sentence = generateSentence(True)
	main_sentence_text = main_sentence[0]
	sentences = [main_sentence_text]
	for i in range(0, 3):
		sentences.append(generateSentence(False))
	random.shuffle(sentences)

	var1, var2, var3, var4 = IntVar(), IntVar(), IntVar(), IntVar()
	op1 = Checkbutton(base, text=sentences[0], variable=var1)
	op1.place(x=10, y=410, width=380, height=100)
	op2 = Checkbutton(base, text=sentences[1], variable=var2)
	op2.place(x=410, y=410, width=380, height=100)
	op3 = Checkbutton(base, text=sentences[2], variable=var3)
	op3.place(x=10, y=530, width=380, height=100)
	op4 = Checkbutton(base, text=sentences[3], variable=var4)
	op4.place(x=410, y=530, width=380, height=100)
	op5 = Button(base, text="Submit", command=lambda : check([var1, var2, var3, var4], sentences, main_sentence_text, canvas))
	op5.place(x=360, y=480, width=100, height=60)

	base.update()
	draw_shapes(canvas)

	base.mainloop()

setup()