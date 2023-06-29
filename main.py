import tkinter as tk

from tkinter import *

def exit_program():
    window.destroy()

window = tk.Tk()  # create root window
window.title("Turing Machine")
window.config(bg="skyblue")

penjumlahan_button = tk.Button(window, text="Penjumlahan")
penjumlahan_button.pack()

pengurangan_button = tk.Button(window, text="Pengurangan")
pengurangan_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()
