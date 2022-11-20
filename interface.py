from tkinter import Tk, Canvas, Button
from draw import shapes
import random

def setup():
	base = Tk()
	base.title("LogiQ")
	base.geometry("800x640")

	canvas = Canvas(base)
	canvas.config(width=800, height=400, bg="white")
	canvas.pack()

	op1 = Button(base, text="∀x(Triangle(x)⇒Blue(x))")
	op1.place(x=10, y=410, width=380, height=100)
	op2 = Button(base, text="∀x(Blue(x)⇒Triangle(x))")
	op2.place(x=410, y=410, width=380, height=100)
	op3 = Button(base, text="∀x(Square(x)⇒Red(x))")
	op3.place(x=10, y=530, width=380, height=100)
	op4 = Button(base, text="∀x(Square(x)⇒Green(x))")
	op4.place(x=410, y=530, width=380, height=100)

	shapes(canvas)

	base.mainloop()

setup()