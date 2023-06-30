
from tkinter import *
from tkinter import ttk
import collections

root = Tk()
root.title("Turing Machine")
root.config(background="lightyellow")

#judul
l1 = Label(text="Pilih Operasi Kalkulator", bg="lightyellow", font="Normal 25")
l1.grid(row=0, column=0, columnspan=4, pady=20, padx=30)

root.mainloop()



"""
from tkinter import Tk, Frame, Entry, Button

# Function to perform calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression entered
        entry.delete(0, 'end')  # Clear the input field
        entry.insert('end', str(result))  # Display the result
    except:
        entry.delete(0, 'end')  # Clear the input field
        entry.insert('end', 'Error')

# Create the main window
root = Tk()
root.title('Calculator')

# Create the calculator frame
calculator_frame = Frame(root)
calculator_frame.pack()

# Create the entry field
entry = Entry(calculator_frame, width=25, font=('Arial', 12))
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    btn = Button(calculator_frame, text=button, width=5, height=2, font=('Arial', 12),
                 command=lambda text=button: entry.insert('end', text))
    btn.grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the equal button
equal_btn = Button(calculator_frame, text='=', width=13, height=2, font=('Arial', 12),
                   command=calculate)
equal_btn.grid(row=row, column=col, columnspan=2)

# Start the GUI event loop
root.mainloop()
"""