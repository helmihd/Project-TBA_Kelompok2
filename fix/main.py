import tkinter as tk
import ctypes
from addition import addition # Mengimport fungsi penjumlahan
from subtraction import subtraction # Mengimport fungsi pengurangan
from multiplication import multiplication # Mengimport fungsi perkalian

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

    button_add = tk.Button(addition_window, text="Jumlahkan", command=perform_addition)
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

    button_add = tk.Button(subtraction_window, text="Jumlahkan", command=perform_subtraction)
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
    multiplication_window.title("Penjumlahan")

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

    button_add = tk.Button(multiplication_window, text="Jumlahkan", command=perform_multiplication)
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

button_exit = tk.Button(main_window, text="Exit", command=exit_program)
button_exit.pack()

main_window.mainloop()
