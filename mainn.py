# file_utama.py
import tkinter as tk
import file_input

def process_input():
    user_input = input_entry.get()
    result = file_input.process_input(user_input)
    label.config(text="Hasil: " + result)

# Membuat jendela utama
window = tk.Tk()
window.title("Contoh GUI Python")

# Membuat label dan input entry
input_label = tk.Label(window, text="Masukkan sebuah teks:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# Membuat tombol
button = tk.Button(window, text="Proses Input", command=process_input)
button.pack()

# Membuat label hasil
label = tk.Label(window, text="Hasil: ")
label.pack()

# Menjalankan event loop
window.mainloop()
