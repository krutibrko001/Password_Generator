from tkinter import *
from tkinter import messagebox
from funcs import Generator
import pyperclip
import sys

generator = Generator()

def exit_funk():
    sys.exit()

def clinks():
    generated_pass = generator.random_generating()
    pyperclip.copy(generated_pass)
    result_pass_entry.delete(0, END)
    result_pass_entry.insert(0, generated_pass)
    # messagebox.showinfo(title='Info', message="Saved to clipboard")
    info_label.config(text="Saved to clipboard.")

# Windows + Image
windows = Tk()
windows.title("Password Generator")
windows.config(padx=20, pady=20)
windows = Canvas(height=200, width=200)
img = PhotoImage(file="ggg.png")
windows.create_image(100, 100, image=img)
windows.grid(row=0, column=1)

#Creating Buttons - Generate
genButton = Button(text="Generate Password",width=14, command=clinks)
genButton.grid(column=1, row=2, columnspan=1)

#Creating Button - Exit
exitButton = Button(text="Exit", width=14, command=exit_funk)
exitButton.grid(column=1, row=3, columnspan=1)

#Creating Empty - Entry
result_pass_entry = Entry(width=17)
result_pass_entry.grid(column=1, row=1, columnspan=1)
result_pass_entry.focus()

# Creating Label - Info
info_label = Label(text="")
info_label.grid(column=1, row=4)


windows.mainloop()


