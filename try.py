import tkinter as tk
import time
from tkinter import ttk
from addition_try import addition

main_window = tk.Tk()
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
                Track_1.append("")

        # Memberi pembatas
        Track_1.append(1)

        # Memasukkan input 2 ke Track 1
        for i in range(abs(num2)):
            if num2 > 0:
                Track_1.append("+")
            elif num2 < 0:
                Track_1.append("-")
            else:
                Track_1.append("")

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

        Track_1_arrow = [" "] * len(Track_1)
        Track_1_arrow[j] = "^"

        Track_2_arrow = [" "] * len(Track_2)
        Track_2_arrow[k] = "^"

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

            time.sleep(2)

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


def exit_program():
    main_window.destroy()


main_window.tk.call("source", "azure.tcl")
main_window.tk.call("set_theme", "dark")

button_addition = ttk.Button(
    main_window, text="Penjumlahan", command=open_addition_window, width=20
)
button_addition.grid(row=0, column=0, ipadx=80, ipady=5, padx=5, pady=5)

main_window.mainloop()
