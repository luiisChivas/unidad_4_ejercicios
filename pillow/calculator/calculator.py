""""Author: Juan Luis Mendiola Gutiérrez
            Juan Pablo Ramírez Ibarra
     email: jlmg67815@gmail.com
            pablo.ram232@gmail.com """
from tkinter import *

root = Tk()
equa = ""

equation = StringVar()
calculation = Label(root, textvariable=equation)
equation.set("Enter your equation: ")
calculation.grid(columnspan=4)


def btn_press(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def equal_press():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""


def clear():
    global equa
    equa = ""
    equation.set("")


Button0 = Button(root, text="0", command=lambda: btn_press(0))
Button0.grid(row=4, column=1)
Button1 = Button(root, text="1", command=lambda: btn_press(1))
Button1.grid(row=1, column=0)
Button2 = Button(root, text="2", command=lambda: btn_press(2))
Button2.grid(row=1, column=1)
Button3 = Button(root, text="3", command=lambda: btn_press(3))
Button3.grid(row=1, column=2)
Button4 = Button(root, text="4", command=lambda: btn_press(4))
Button4.grid(row=2, column=0)
Button5 = Button(root, text="5", command=lambda: btn_press(5))
Button5.grid(row=2, column=1)
Button6 = Button(root, text="6", command=lambda: btn_press(6))
Button6.grid(row=2, column=2)
Button7 = Button(root, text="7", command=lambda: btn_press(7))
Button7.grid(row=3, column=0)
Button8 = Button(root, text="8", command=lambda: btn_press(8))
Button8.grid(row=3, column=1)
Button9 = Button(root, text="9", command=lambda: btn_press(9))
Button9.grid(row=3, column=2)
Plus = Button(root, text="+", command=lambda: btn_press("+"))
Plus.grid(row=1, column=3)
Minus = Button(root, text="-", command=lambda: btn_press("-"))
Minus.grid(row=2, column=3)
Multiply = Button(root, text="*", command=lambda: btn_press("*"))
Multiply.grid(row=3, column=3)
Didive = Button(root, text="/", command=lambda: btn_press("/"))
Didive.grid(row=4, column=3)
Equal = Button(root, text="=", command=equal_press)
Equal.grid(row=4, column=2)
Clear = Button(root, text="C", command=clear)
Clear.grid(row=4, column=0)


root.mainloop()