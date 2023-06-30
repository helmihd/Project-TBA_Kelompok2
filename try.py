import tkinter as tk
from tkinter import Tk, ttk, Button
from addition import addition
from subtraction import subtraction
from multiplication import multiplication

main_window = Tk()
main_window.title("Program Turing Machine")

def open_addition_window():    
    addition_window = tk.Tk()
    addition_window.tk.call("source", "azure.tcl")
    addition_window.tk.call("set_theme", "dark")
    addition_window.title("Penjumlahan")
    addition_window.geometry('700x400')  # Ukuran tetap (lebar x tinggi)
    addition_window.resizable(False, False)  # Mengunci ukuran jendela

    #addition_window.geometry(main_window.geometry())
    
    main_window.withdraw()  # Menyembunyikan jendela utama

    def perform_addition():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, result = addition(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_result.config(text="Hasil: " + str(result))
    
    def back_to_main_window():
        addition_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama
    
    label_num1 = ttk.Label(addition_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = ttk.Entry(addition_window)
    entry_num1.pack()

    label_num2 = ttk.Label(addition_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = ttk.Entry(addition_window)
    entry_num2.pack()

    button_add = ttk.Button(addition_window, text="Hitung", command=perform_addition)
    button_add.pack()
    
    label_track_1 = ttk.Label(addition_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(addition_window, text="Track 2: ")
    label_track_2.pack()

    label_result = ttk.Label(addition_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(addition_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_subtraction_window():
    subtraction_window = tk.Tk()
    subtraction_window.tk.call("source", "azure.tcl")
    subtraction_window.tk.call("set_theme", "dark")
    subtraction_window.title("Pengurangan")
    subtraction_window.geometry('700x400')  # Ukuran tetap (lebar x tinggi)
    subtraction_window.resizable(False, False)  # Mengunci ukuran jendela

    main_window.withdraw() 

    def perform_subtraction():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, result = subtraction(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        subtraction_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = ttk.Label(subtraction_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = ttk.Entry(subtraction_window)
    entry_num1.pack()

    label_num2 = ttk.Label(subtraction_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = ttk.Entry(subtraction_window)
    entry_num2.pack()

    button_add = ttk.Button(subtraction_window, text="Hitung", command=perform_subtraction)
    button_add.pack()
    
    label_track_1 = ttk.Label(subtraction_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(subtraction_window, text="Track 2: ")
    label_track_2.pack()

    label_result = ttk.Label(subtraction_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(subtraction_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_multiplication_window():
    multiplication_window = tk.Tk()
    multiplication_window.tk.call("source", "azure.tcl")
    multiplication_window.tk.call("set_theme", "dark")
    multiplication_window.title("Pengurangan")
    multiplication_window.geometry('700x400')  # Ukuran tetap (lebar x tinggi)
    multiplication_window.resizable(False, False)  # Mengunci ukuran jendela

    main_window.withdraw()

    def perform_multiplication():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, Track_3, result = multiplication(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 2: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        multiplication_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = ttk.Label(multiplication_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = ttk.Entry(multiplication_window)
    entry_num1.pack()

    label_num2 = ttk.Label(multiplication_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = ttk.Entry(multiplication_window)
    entry_num2.pack()

    button_add = ttk.Button(multiplication_window, text="Hitung", command=perform_multiplication)
    button_add.pack()
    
    label_track_1 = ttk.Label(multiplication_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(multiplication_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(multiplication_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(multiplication_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(multiplication_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def exit_program():
    main_window.destroy()

main_window.tk.call("source", "azure.tcl")
main_window.tk.call("set_theme", "dark")
main_window.geometry('700x400')  # Ukuran tetap (lebar x tinggi)
main_window.resizable(False, False)  # Mengunci ukuran jendela

#main_window.geometry("400x300")  # Mengatur lebar=400 dan tinggi=300 piksel
# Mengukur tinggi taskbar
"""
taskbar_height = main_window.winfo_screenheight() - main_window.winfo_vrootheight()
screen_width = main_window.winfo_screenwidth()


# Mengatur ukuran jendela dengan mempertimbangkan tinggi taskbar
window_width = screen_width
window_height = main_window.winfo_screenheight() - taskbar_height

# Mengatur ukuran jendela
main_window.geometry(f"{window_width}x{window_height}")
main_window.geometry(f"+0+0")
"""
#main_window.resizable(False, False)


button_addition = ttk.Button(main_window, text="Penjumlahan", command=open_addition_window, width=20)
button_addition.grid(row=0, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_subtraction = ttk.Button(main_window, text="Pengurangan", command=open_subtraction_window, width=20)
button_subtraction.grid(row=0, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_multiplication = ttk.Button(main_window, text="Perkalian", command=open_multiplication_window,width=20)
button_multiplication.grid(row=1, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_distribution = ttk.Button(main_window, text="Pembagian", width=20)
button_distribution.grid(row=1, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_factorial = ttk.Button(main_window, text="Faktorial", width=20)
button_factorial.grid(row=2, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_power = ttk.Button(main_window, text="Perpangkatan", width=20)
button_power.grid(row=2, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_root = ttk.Button(main_window, text="Akar Kuadrat", width=20)
button_root.grid(row=3, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_exit = ttk.Button(main_window, text="Exit", width=20, command=exit_program)
button_exit.grid(row=3, column=1, ipadx=80, ipady=5, padx=5, pady=5)
# button_exit.pack()

main_window.mainloop()