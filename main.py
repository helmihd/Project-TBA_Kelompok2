import tkinter as tk
import ctypes
from tkinter import ttk
from ttkthemes import ThemedTk
from addition import addition # Mengimport fungsi penjumlahan
from subtraction import subtraction # Mengimport fungsi pengurangan
from multiplication import multiplication # Mengimport fungsi perkalian
from distribution import distribution # Mengimport fungsi pembagian
from factorial import factorial # Mengimport fungsi faktorial
from power import power # Mengimport fungsi pangkat
from root import root # Mengimport fungsi akar

"""
def set_window_fullscreen(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    taskbar_height = get_taskbar_height()

    window.geometry(f"{screen_width}x{screen_height - taskbar_height}")

def get_taskbar_height():
    taskbar_height = 0

    if ctypes.windll.user32.GetSystemMetrics(0x02) != 0:  # 0x02 mengindikasikan taskbar di bawah
        taskbar_height = ctypes.windll.user32.GetSystemMetrics(0x02) 

    return taskbar_height
"""
def open_addition_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    addition_window = tk.Toplevel()
    addition_window.title("Penjumlahan")

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

    label_num1 = tk.Label(addition_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = tk.Entry(addition_window)
    entry_num1.pack()

    label_num2 = tk.Label(addition_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = tk.Entry(addition_window)
    entry_num2.pack()

    button_add = tk.Button(addition_window, text="Hitung", command=perform_addition)
    button_add.pack()
    
    label_track_1 = tk.Label(addition_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(addition_window, text="Track 2: ")
    label_track_2.pack()

    label_result = tk.Label(addition_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(addition_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_subtraction_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    subtraction_window = tk.Toplevel()
    subtraction_window.title("Pengurangan")

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

    label_num1 = tk.Label(subtraction_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = tk.Entry(subtraction_window)
    entry_num1.pack()

    label_num2 = tk.Label(subtraction_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = tk.Entry(subtraction_window)
    entry_num2.pack()

    button_add = tk.Button(subtraction_window, text="Hitung", command=perform_subtraction)
    button_add.pack()
    
    label_track_1 = tk.Label(subtraction_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(subtraction_window, text="Track 2: ")
    label_track_2.pack()

    label_result = tk.Label(subtraction_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(subtraction_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
   
def open_multiplication_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    multiplication_window = tk.Toplevel()
    multiplication_window.title("Perkalian")

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

    label_num1 = tk.Label(multiplication_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = tk.Entry(multiplication_window)
    entry_num1.pack()

    label_num2 = tk.Label(multiplication_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = tk.Entry(multiplication_window)
    entry_num2.pack()

    button_add = tk.Button(multiplication_window, text="Hitung", command=perform_multiplication)
    button_add.pack()
    
    label_track_1 = tk.Label(multiplication_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(multiplication_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = tk.Label(multiplication_window, text="Track 3: ")
    label_track_3.pack()

    label_result = tk.Label(multiplication_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(multiplication_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
  
def open_distribution_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    distribution_window = tk.Toplevel()
    distribution_window.title("Pembagian")

    def perform_distribution():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, Track_3, result = distribution(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 2: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        distribution_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = tk.Label(distribution_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = tk.Entry(distribution_window)
    entry_num1.pack()

    label_num2 = tk.Label(distribution_window, text="Bilangan 2:")
    label_num2.pack()

    entry_num2 = tk.Entry(distribution_window)
    entry_num2.pack()

    button_add = tk.Button(distribution_window, text="Hitung", command=perform_distribution)
    button_add.pack()
    
    label_track_1 = tk.Label(distribution_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(distribution_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = tk.Label(distribution_window, text="Track 3: ")
    label_track_3.pack()

    label_result = tk.Label(distribution_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(distribution_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
   
def open_factorial_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    factorial_window = tk.Toplevel()
    factorial_window.title("Faktorial")

    def perform_factorial():
        num1 = int(entry_num1.get())
        Track_1, Track_2, Track_3, result = factorial(num1)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        factorial_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = tk.Label(factorial_window, text="Bilangan 1:")
    label_num1.pack()

    entry_num1 = tk.Entry(factorial_window)
    entry_num1.pack()

    button_add = tk.Button(factorial_window, text="Hitung", command=perform_factorial)
    button_add.pack()
    
    label_track_1 = tk.Label(factorial_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(factorial_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = tk.Label(factorial_window, text="Track 3: ")
    label_track_3.pack()

    label_result = tk.Label(factorial_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(factorial_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
    
def open_power_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    power_window = tk.Toplevel()
    power_window.title("Perpangkatan")

    def perform_power():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, Track_3, result = power(num1, num2)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        power_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = tk.Label(power_window, text="Masukkan bilangan basis:")
    label_num1.pack()

    entry_num1 = tk.Entry(power_window)
    entry_num1.pack()
    
    label_num2 = tk.Label(power_window, text="Masukkan bilangan pangkat:")
    label_num2.pack()
    
    entry_num2 = tk.Entry(power_window)
    entry_num2.pack()

    button_add = tk.Button(power_window, text="Hitung", command=perform_power)
    button_add.pack()
    
    label_track_1 = tk.Label(power_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(power_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = tk.Label(power_window, text="Track 3: ")
    label_track_3.pack()

    label_result = tk.Label(power_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(power_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def open_root_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    root_window = tk.Toplevel()
    root_window.title("Akar Kuadrat")

    def perform_root():
        num1 = int(entry_num1.get())
        Track_1, Track_2, Track_3, result = root(num1)
        label_track_1.config(text="Track 1: " + ''.join(str(x) for x in Track_1))
        label_track_2.config(text="Track 2: " + ''.join(str(x) for x in Track_2))
        label_track_3.config(text="Track 3: " + ''.join(str(x) for x in Track_3))
        label_result.config(text="Hasil: " + str(result))
        
    def back_to_main_window():
        root_window.destroy()  # Menutup jendela penjumlahan
        main_window.deiconify()  # Membuka kembali jendela utama

    label_num1 = tk.Label(root_window, text="Masukkan bilangan yang ingin diakarkan:")
    label_num1.pack()

    entry_num1 = tk.Entry(root_window)
    entry_num1.pack()

    button_add = tk.Button(root_window, text="Hitung", command=perform_root)
    button_add.pack()
    
    label_track_1 = tk.Label(root_window, text="Track 1 :")
    label_track_1.pack()
    
    label_track_2 = tk.Label(root_window, text="Track 2: ")
    label_track_2.pack()
    
    label_track_3 = tk.Label(root_window, text="Track 3: ")
    label_track_3.pack()

    label_result = tk.Label(root_window, text="Hasil: ")
    label_result.pack()
    
    button_back = tk.Button(root_window, text="Kembali", command=back_to_main_window)
    button_back.pack()
    
def exit_program():
    main_window.destroy()

main_window = tk.Tk()
main_window.title("Program Kalkulator")

# set_window_fullscreen(main_window)

button_addition = tk.Button(main_window, text="Penjumlahan", command=open_addition_window)
button_addition.pack()

button_subtraction = tk.Button(main_window, text="Pengurangan", command=open_subtraction_window)
button_subtraction.pack()

button_multiplication = tk.Button(main_window, text="Perkalian", command=open_multiplication_window)
button_multiplication.pack()

button_distribution = tk.Button(main_window, text="Pembagian", command=open_distribution_window)
button_distribution.pack()

button_factorial = tk.Button(main_window, text="Faktorial", command=open_factorial_window)
button_factorial.pack()

button_power = tk.Button(main_window, text="Perpangkatan", command=open_power_window)
button_power.pack()

button_root = tk.Button(main_window, text="Akar kuadart", command=open_root_window)
button_root.pack()

button_exit = tk.Button(main_window, text="Exit", command=exit_program)
button_exit.pack()

main_window.mainloop()