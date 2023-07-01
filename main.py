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

        for i in range(len(Track_1)):
            Track_2.append("B")

        j = abs(num1) + abs(num2) + 1
        k = abs(num1) + abs(num2) + 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        # Initial State q0
        q = 0        
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            addition_window.update()
        
        while q not in [3, 5, 7, 9, 10]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k = addition(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k
            )

            time.sleep(0.5)
    
        update_table()

        a = Track_2.count("+")
        b = Track_2.count("-")

        if a > b:
            result = a
        elif a == b:
            result = 0
        else:
            result = -b
            
        label_result.config(text="Hasil: " + str(result))
        
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


    track_1_values_frame = ttk.LabelFrame(addition_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(addition_window)
    track_1_arrow_values_frame.pack()


    track_2_values_frame = ttk.LabelFrame(addition_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(addition_window)
    track_2_arrow_values_frame.pack()

    label_result = ttk.Label(addition_window, text="Hasil: ")
    label_result.pack()

    button_back = ttk.Button(addition_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

    addition_window.mainloop()

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
        # Mendeklarasikan 2 track kosong
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

        for i in range(len(Track_1)):
            Track_2.append("B")

        j = abs(num1) + abs(num2) + 1
        k = abs(num1) + abs(num2) + 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            subtraction_window.update()
            
        while q not in [3, 5, 6, 8, 10, 11]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k = subtraction(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k
            )

            time.sleep(0.5)
            
        update_table()
        
        a = Track_2.count("+")
        b = Track_2.count("-")

        if a > b:
            result = a
        elif a == b:
            result = 0
        else:
            result = -b
            
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

    track_1_values_frame = ttk.LabelFrame(subtraction_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(subtraction_window)
    track_1_arrow_values_frame.pack()


    track_2_values_frame = ttk.LabelFrame(subtraction_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(subtraction_window)
    track_2_arrow_values_frame.pack()

    label_result = ttk.Label(subtraction_window, text="Hasil: ")
    label_result.pack()

    button_back = ttk.Button(subtraction_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

    subtraction_window.mainloop()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []

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
        Track_1.append(1)


        # Menambahkan blank di awal dan akhir di semua track
        for i in range(abs(num1) * abs(num2) + 1):
            Track_1.insert(0, "B")
            Track_1.append("B")
            
        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")

        # Menentukan posisi awal pada masing-masing Track
        j = abs(num1) * abs(num2) + 1
        k = abs(num1) * abs(num2) + 1
        l = abs(num1) * abs(num2) + 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            multiplication_window.update()
            
        while q not in [4]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = multiplication(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        a = Track_3.count("+")
        b = Track_3.count("-")
        
        if a > b:
            result = a
        elif a == b:
            result = 0
        else:
            result = -b
            
        label_result.config(text="Hasil: " + str(result))

    def back_to_main_window():
        multiplication_window.destroy()
        main_window.deiconify()

    label_num1 = ttk.Label(multiplication_window, text="Masukkan bilangan pertama:")
    label_num1.pack()

    entry_num1 = ttk.Entry(multiplication_window)
    entry_num1.pack()

    label_num2 = ttk.Label(multiplication_window, text="Masukkan bilangan kedua:")
    label_num2.pack()

    entry_num2 = ttk.Entry(multiplication_window)
    entry_num2.pack()

    button_add = ttk.Button(multiplication_window, text="Hitung", command=perform_multiplication)
    button_add.pack()
    
    track_1_values_frame = ttk.LabelFrame(multiplication_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(multiplication_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(multiplication_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(multiplication_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(multiplication_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(multiplication_window)
    track_3_arrow_values_frame.pack()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []

        # Memasukkan input bilangan penyebut ke Track 1
        for i in range(abs(num2)):
            if num2 > 0:
                Track_1.append("+")
            elif num2 < 0:
                Track_1.append("-")
            else:
                Track_1.append()

        # Memberi pembatas
        Track_1.append(1)

        # Memasukkan input bilangan pembilang Track 1
        for i in range(abs(num1)):
            if num1 > 0:
                Track_1.append("+")
            elif num1 < 0:
                Track_1.append("-")
            else:
                Track_1.append()

        # Menambahkan blank di awal dan akhir di semua track
        for i in range(abs(num1) * abs(num2) + 1):
            Track_1.insert(0, "B")
            Track_1.append("B")
            
        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")
        
        # Menentukan posisi awal pada masing-masing Track
        j = abs(num1) * abs(num2) + 1
        k = abs(num1) * abs(num2) + 1
        l = abs(num1) * abs(num2) + 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            distribution_window.update()
            
        while q not in [4, 7, 8]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = distribution(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        a = Track_3.count("+")
        b = Track_3.count("-")

        if a > b:
            result = a
        elif a == b:
            result = 0
        else:
            result = -b
    
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
    
    track_1_values_frame = ttk.LabelFrame(distribution_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(distribution_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(distribution_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(distribution_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(distribution_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(distribution_window)
    track_3_arrow_values_frame.pack()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []
        
        Track_1.append("B")
        # Memasukkan input ke Track 1
        for i in range(abs(num1)):
            Track_1.append(0)
            
        # Memberi pembatas
        Track_1.append(1)
            
        # Fungsi untuk menambah blank di belakang track
        def count_factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * count_factorial(n - 1)
            
        # Menambahkan blank di awal dan akhir di semua track sebanyak factorial dari input
        for i in range(count_factorial(num1) + 1):
            Track_1.append("B")
            
        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")

        # Menentukan posisi awal pada masing-masing Track
        j = 1
        k = 1
        l = 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            factorial_window.update()
            
        while q not in [5, 6]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = factorial(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        result = Track_3.count(0)
        
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
    
    track_1_values_frame = ttk.LabelFrame(factorial_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(factorial_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(factorial_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(factorial_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(factorial_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(factorial_window)
    track_3_arrow_values_frame.pack()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []

        # Memasukkan input 1 ke Track 1
        for i in range(abs(num1)):
            Track_1.append(0)

        # Memberi pembatas
        Track_1.append(1)

        # Memasukkan input 2 ke Track 1
        for i in range(abs(num2)):
            Track_1.append(0)

        # Menambahkan blank di awal dan akhir di semua track
        for i in range(abs(num1) ** abs(num2) + 1):
            Track_1.append("B")
        Track_1.insert(0, "B")

        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")

        # Menentukan posisi awal pada masing-masing Track
        j = 1
        k = 1
        l = 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            power_window.update()
            
        while q not in [9, 10, 12]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = power(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        result = Track_3.count(0)
        
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
    
    track_1_values_frame = ttk.LabelFrame(power_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(power_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(power_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(power_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(power_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(power_window)
    track_3_arrow_values_frame.pack()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []

        # Memberi pembatas
        Track_1.append(1)

        # Memasukkan input ke Track 1
        for i in range(abs(num1)):
            Track_1.append(0)

        # Menambahkan blank di awal dan akhir Track
        for i in range(num1):
            Track_1.insert(0, "B")
        Track_1.insert(0, "B")
        Track_1.append("B")

        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")

        # Menentukan posisi awal pada masing-masing Track
        j = num1 + 1
        k = num1 + 1
        l = num1 + 1
        
        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            root_window.update()
            
        while q not in [8]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = root(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        index = Track_1.index(1)
        result = Track_1[:index].count(0)
        
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
    
    track_1_values_frame = ttk.LabelFrame(root_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(root_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(root_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(root_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(root_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(root_window)
    track_3_arrow_values_frame.pack()

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
        # Mendeklarasikan 3 track kosong
        Track_1 = []
        Track_2 = []
        Track_3 = []

        # Memasukkan input 1 ke Track 1
        for i in range(abs(num1)):
            Track_1.append(0)

        # Menambahkan blank di awal dan akhir di semua track
        for i in range(num1 + 1):
            Track_1.append("B")
        for i in range(num1 + 1):
            Track_1.insert(0, "B")
        Track_1.append("B")

        for i in range(len(Track_1)):
            Track_2.append("B")
            Track_3.append("B")
            
        # Menentukan posisi awal pada masing-masing Track
        j = num1 + 1
        k = num1 + 1
        l = num1 + 1

        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"
        
        Track_3_arrow = [" "] * len(Track_3)
        Track_3_arrow[l] = "^"
        
        # Initial State q0
        q = 0
        
        def update_table():
            # Hapus konten pada LabelFrame
            for child in track_1_values_frame.winfo_children():
                child.destroy()
            for child in track_1_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_2_values_frame.winfo_children():
                child.destroy()
            for child in track_2_arrow_values_frame.winfo_children():
                child.destroy()
            for child in track_3_values_frame.winfo_children():
                child.destroy()
            for child in track_3_arrow_values_frame.winfo_children():
                child.destroy()

            # Perbarui LabelFrame dengan nilai Track 1 dan panah
            for value in Track_1:
                label = ttk.Label(track_1_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_1_arrow:
                label = ttk.Label(track_1_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2:
                label = ttk.Label(track_2_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_2_arrow:
                label = ttk.Label(track_2_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3:
                label = ttk.Label(track_3_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")
            for value in Track_3_arrow:
                label = ttk.Label(track_3_arrow_values_frame, text=value, width=1, anchor="center")
                label.pack(side="left")

            logarithm_window.update()
            
        while q not in [9]:
            update_table()
            Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l = logarithm(
                Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l
            )

            time.sleep(0.5)
            
        update_table()
        
        a = Track_3.count(0)
        if a > 0:
            result = a
        else:
            result = "Hasil tidak valid"
        
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
    
    track_1_values_frame = ttk.LabelFrame(logarithm_window, text="Track 1")
    track_1_values_frame.pack()

    track_1_arrow_values_frame = ttk.LabelFrame(logarithm_window)
    track_1_arrow_values_frame.pack()
    
    track_2_values_frame = ttk.LabelFrame(logarithm_window, text="Track 2")
    track_2_values_frame.pack()

    track_2_arrow_values_frame = ttk.LabelFrame(logarithm_window)
    track_2_arrow_values_frame.pack()
    
    track_3_values_frame = ttk.LabelFrame(logarithm_window, text="Track 3")
    track_3_values_frame.pack()

    track_3_arrow_values_frame = ttk.LabelFrame(logarithm_window)
    track_3_arrow_values_frame.pack()

    label_result = ttk.Label(logarithm_window, text="Hasil: ")
    label_result.pack()
    
    button_back = ttk.Button(logarithm_window, text="Kembali", command=back_to_main_window)
    button_back.pack()

def exit_program():
    main_window.destroy()

main_window.tk.call("source", "azure.tcl")
main_window.tk.call("set_theme", "dark")

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