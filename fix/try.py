import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Program Turing Machine")

def exit_program():
    main_window.destroy()

main_window.tk.call("source", "azure.tcl")
main_window.tk.call("set_theme", "dark")

button_exit = ttk.Button(main_window, text="Exit", command=exit_program)
button_exit.pack()

main_window.mainloop()