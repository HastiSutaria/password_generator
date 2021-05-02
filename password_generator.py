import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def low():
	entry.delete(0, END)

	length = x.get()

	lower = "abcdefghijklmnopqrstuvwxyz"
	ul = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	mix = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	password = ""

	if var.get() == 1:
		for i in range(0, length):
			password = password + random.choice(lower)
		return password

	elif var.get() == 0:
		for i in range(0, length):
			password = password + random.choice(ul)
		return password

	elif var.get() == 2:
		for i in range(0, length):
			password = password + random.choice(mix)
		return password
	else:
		print("Please choose an option")

def generate():
	password1 = low()
	entry.insert(10, password1)

def copy1():
	random_password = entry.get()
	pyperclip.copy(random_password)

root = Tk()
var = IntVar()
x = IntVar()

root.title("Random Password Generator")
root.geometry("400x200")
root.configure(bg='light blue')

c_label = Label(root, text="Length")
c_label.grid(row=1)


label2 = Label(root, text ="Strength" )
label2.grid(row = 3, column = 0)


radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=3, column=1, sticky='W')
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=4, column=1, sticky='W')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=2)
radio_strong.grid(row=5, column=1, sticky='W')
combo = Combobox(root, textvariable=x)

combo['values'] = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=7, column=1)



Random_password = Label(root, text="Password")
Random_password.grid(row=9)

entry = Entry(root)
entry.grid(row=9, column=1)
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=11, column=1)


root.mainloop()
