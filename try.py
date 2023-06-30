def open_multiplication_window():
    main_window.withdraw()  # Menyembunyikan jendela utama

    multiplication_window = tk.Toplevel()
    multiplication_window.title("Penjumlahan")

    def perform_multiplication():
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        Track_1, Track_2, result = multiplication(num1, num2)
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