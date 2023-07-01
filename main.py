import tkinter as tk
import time
from tkinter import Tk, ttk, Button

from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from distribution import distribution
from factorial import factorial
from power import power
from root import root
from logarithm import logarithm

main_window = Tk()
main_window.title("Program Turing Machine")

def open_addition_window():    
    addition_window = tk.Tk()
    addition_window.tk.call("source", "azure.tcl")
    addition_window.tk.call("set_theme", "dark")
    addition_window.title("Penjumlahan")
    addition_window.geometry(main_window.geometry())
    
    main_window.withdraw()

    def perform_addition():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1 = []
        Track_2 = []

        # Memasukkan input 1 ke Track 1
        for i in range(abs(num1)):
            if num1 > 0:
                Track_1.append("+")
            elif num1 < 0:
                Track_1.append("-")
            else:
                Track_1.append()

        # Memberi pembatas
        Track_1.append(1)

        # Memasukkan input 2 ke Track 1
        for i in range(abs(num2)):
            if num2 > 0:
                Track_1.append("+")
            elif num2 < 0:
                Track_1.append("-")
            else:
                Track_1.append()

        # Menambahkan blank di awal dan akhir di kedua track
        for i in range(abs(num1) + abs(num2) + 1):
            Track_1.insert(0, "B")
            Track_1.append("B")

        for i in range(abs(num1) + abs(num2)):
            Track_2.append("B")
            Track_2.append("B")
            Track_2.append("B")
        Track_2.append("B")
        Track_2.append("B")
        Track_2.append("B")

        j = abs(num1) + abs(num2) + 1
        k = abs(num1) + abs(num2) + 1
        # Initial State q0
        q = 0        
        
        while q not in [3, 5, 7, 9, 10]:
            label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
            label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
            Track_1, Track_2, q, j, k = addition(Track_1, Track_2, q, j, k)           

            time.sleep(1)
            addition_window.update()
    
    def back_to_main_window():
        addition_window.destroy()
        main_window.deiconify() 
    
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
    subtraction_window.geometry(main_window.geometry())

    main_window.withdraw() 

    def perform_subtraction():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, result = subtraction(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        subtraction_window.destroy()
        main_window.deiconify() 

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
    multiplication_window.title("Perkalian")
    multiplication_window.geometry(main_window.geometry())
    
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
        multiplication_window.destroy()
        main_window.deiconify()

    label_num1 = ttk.Label(multiplication_window, text="Masukkan bilangan pembilang:")
    label_num1.pack()

    entry_num1 = ttk.Entry(multiplication_window)
    entry_num1.pack()

    label_num2 = ttk.Label(multiplication_window, text="Masukkan bilangan penyebut:")
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

def open_distribution_window():
    distribution_window = tk.Tk()
    distribution_window.tk.call("source", "azure.tcl")
    distribution_window.tk.call("set_theme", "dark")
    distribution_window.title("Pembagian")
    distribution_window.geometry(main_window.geometry())

    main_window.withdraw()

    def perform_distribution():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, Track_3, result = distribution(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 2: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        distribution_window.destroy()
        main_window.deiconify()

    label_num1 = ttk.Label(distribution_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = ttk.Entry(distribution_window)
    entry_num1.pack()

    label_num2 = ttk.Label(distribution_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = ttk.Entry(distribution_window)
    entry_num2.pack()

    button_add = ttk.Button(distribution_window, text="Hitung", command=perform_distribution)
    button_add.pack()
    
    label_track_1 = ttk.Label(distribution_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(distribution_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(distribution_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(distribution_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(distribution_window, text="Kembali", command=back_to_main_window)
    button_back.pack()    

def open_factorial_window():
    factorial_window = tk.Tk()
    factorial_window.tk.call("source", "azure.tcl")
    factorial_window.tk.call("set_theme", "dark")
    factorial_window.title("Faktorial")    
    factorial_window.geometry(main_window.geometry())

    
    main_window.withdraw()

    def perform_factorial():
        num1 = int(entry_num1.get())
        Track_1, Track_2, Track_3, result = factorial(num1)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        factorial_window.destroy()
        main_window.deiconify() 

    label_num1 = ttk.Label(factorial_window, text="Masukkan bilangan yang ingin difaktorialkan:")
    label_num1.pack()

    entry_num1 = ttk.Entry(factorial_window)
    entry_num1.pack()

    button_add = ttk.Button(factorial_window, text="Hitung", command=perform_factorial)
    button_add.pack()
    
    label_track_1 = ttk.Label(factorial_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(factorial_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(factorial_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(factorial_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(factorial_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_power_window():
    power_window = tk.Tk()
    power_window.tk.call("source", "azure.tcl")
    power_window.tk.call("set_theme", "dark")
    power_window.title("Perpangkatan")    
    power_window.geometry(main_window.geometry())

    main_window.withdraw()

    def perform_power():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, Track_3, result = power(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        power_window.destroy()
        main_window.deiconify() 

    label_num1 = ttk.Label(power_window, text="Masukkan bilangan basis:")
    label_num1.pack()

    entry_num1 = ttk.Entry(power_window)
    entry_num1.pack()
    
    label_num2 = ttk.Label(power_window, text="Masukkan bilangan pangkat:")
    label_num2.pack()
    
    entry_num2 = ttk.Entry(power_window)
    entry_num2.pack()

    button_add = ttk.Button(power_window, text="Hitung", command=perform_power)
    button_add.pack()
    
    label_track_1 = ttk.Label(power_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(power_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(power_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(power_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(power_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_root_window():
    root_window = tk.Tk()
    root_window.tk.call("source", "azure.tcl")
    root_window.tk.call("set_theme", "dark")
    root_window.title("Akar Kuadrat")
    root_window.geometry(main_window.geometry())
    
    main_window.withdraw()

    def perform_root():
        num1 = int(entry_num1.get())
        Track_1, Track_2, Track_3, result = root(num1)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        root_window.destroy()
        main_window.deiconify() 

    label_num1 = ttk.Label(root_window, text="Masukkan bilangan yang ingin diakarkan:")
    label_num1.pack()

    entry_num1 = ttk.Entry(root_window)
    entry_num1.pack()

    button_add = ttk.Button(root_window, text="Hitung", command=perform_root)
    button_add.pack()
    
    label_track_1 = ttk.Label(root_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(root_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(root_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(root_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(root_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
    
def open_logarithm_window():
    logarithm_window = tk.Tk()
    logarithm_window.tk.call("source", "azure.tcl")
    logarithm_window.tk.call("set_theme", "dark")
    logarithm_window.title("Logaritma Biner")    
    logarithm_window.geometry(main_window.geometry())
    
    main_window.withdraw()

    def perform_logarithm():
        num1 = int(entry_num1.get())
        Track_1, Track_2, Track_3, result = logarithm(num1)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        logarithm_window.destroy()
        main_window.deiconify() 

    label_num1 = ttk.Label(logarithm_window, text="Masukkan bilangan pokok:")
    label_num1.pack()

    entry_num1 = ttk.Entry(logarithm_window)
    entry_num1.pack()

    button_add = ttk.Button(logarithm_window, text="Hitung", command=perform_logarithm)
    button_add.pack()
    
    label_track_1 = ttk.Label(logarithm_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = ttk.Label(logarithm_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = ttk.Label(logarithm_window, text="Track 3: ")
    label_track_3.pack()

    label_result = ttk.Label(logarithm_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(logarithm_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def exit_program():
    main_window.destroy()

main_window.tk.call("source", "azure.tcl")
main_window.tk.call("set_theme", "dark")

"""
main_window.geometry('700x400')  # Ukuran tetap (lebar x tinggi)
main_window.resizable(False, False)  # Mengunci ukuran jendela
"""
button_addition = ttk.Button(main_window, text="Penjumlahan", command=open_addition_window, width=20)
button_addition.grid(row=0, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_subtraction = ttk.Button(main_window, text="Pengurangan", command=open_subtraction_window, width=20)
button_subtraction.grid(row=0, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_multiplication = ttk.Button(main_window, text="Perkalian", command=open_multiplication_window, width=20)
button_multiplication.grid(row=1, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_distribution = ttk.Button(main_window, text="Pembagian", command=open_distribution_window, width=20)
button_distribution.grid(row=1, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_factorial = ttk.Button(main_window, text="Faktorial", command=open_factorial_window, width=20)
button_factorial.grid(row=2, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_power = ttk.Button(main_window, text="Perpangkatan", comman=open_power_window, width=20)
button_power.grid(row=2, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_root = ttk.Button(main_window, text="Akar Kuadrat", command=open_root_window, width=20)
button_root.grid(row=3, column=0, ipadx=80, ipady=5, padx=5, pady=5)

button_logarithm = ttk.Button(main_window, text="Logaritma Biner", command=open_logarithm_window, width=20)
button_logarithm.grid(row=3, column=1, ipadx=80, ipady=5, padx=5, pady=5)

button_exit = ttk.Button(main_window, text="Exit", width=20, command=exit_program)
button_exit.grid(row=4, column=0, columnspan=2, ipadx=80, ipady=5, padx=5, pady=5)

main_window.mainloop()