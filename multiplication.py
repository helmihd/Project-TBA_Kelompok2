def multiplication(num1, num2):
    # Mendeklarasikan 3 track kosong
    Track_1 = []
    Track_2 = []
    Track_3 = []

    # Memasukkan input bilangan pertama
    input_1 = num1

    # Memasukkan input bilangan kedua
    input_2 = num2

    # Memasukkan input 1 ke Track 1
    for i in range(abs(input_1)):
        if input_1 > 0:
            Track_1.append("+")
        elif input_1 < 0:
            Track_1.append("-")
        else:
            Track_1.append()

    # Memberi pembatas
    Track_1.append(1)

    # Memasukkan input 2 ke Track 1
    for i in range(abs(input_2)):
        if input_2 > 0:
            Track_1.append("+")
        elif input_2 < 0:
            Track_1.append("-")
        else:
            Track_1.append()
    Track_1.append(1)


    # Menambahkan blank di awal dan akhir di semua track
    for i in range(abs(input_1) * abs(input_2) + 1):
        Track_1.insert(0, "B")
        Track_1.append("B")
        
    for i in range(abs(input_1) * abs(input_2)):
        Track_2.append("B")
        Track_2.append("B")
    for i in range(abs(input_1) + abs(input_2) + 2):
        Track_2.append("B")
    Track_2.append("B")
    Track_2.append("B")

    for i in range(abs(input_1) * abs(input_2)):
        Track_3.append("B")
        Track_3.append("B")
    for i in range(abs(input_1) + abs(input_2) + 2):
        Track_3.append("B")
    Track_3.append("B")
    Track_3.append("B")

    # Menentukan posisi awal pada masing-masing Track
    j = abs(input_1) * abs(input_2) + 1
    k = abs(input_1) * abs(input_2) + 1
    l = abs(input_1) * abs(input_2) + 1
    # Initial State q0
    q = 0

    while q not in [4]:
        # State q0
        if q == 0:       
            if Track_1[j] == "+":
                Track_2[k] = Track_1[j]
                Track_1[j] = "B"
                j += 1
                k += 1
                q = 1
            elif Track_1[j] == "-":
                Track_2[k] = Track_1[j]
                Track_1[j] = "B"
                j += 1
                k += 1
                q = 1
            elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
                Track_3[l] = 1
                q = 4
        # State q1
        elif q == 1:
            if Track_1[j] == "+" and Track_2[k] == "B" and Track_3[l] == "B":
                j += 1
                q = 1
            elif Track_1[j] == "-" and Track_2[k] == "B" and Track_3[l] == "B":
                j += 1
                q = 1
            elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
                j += 1
                k -= 1
                q = 2
        # State q2
        elif q == 2:
            if Track_1[j] == "+" and Track_2[k] == "+" and Track_3[l] == "B":
                Track_3[l] = "+"
                j += 1
                l += 1
                q = 2
            elif Track_1[j] == "-" and Track_2[k] == "-" and Track_3[l] == "B":
                Track_3[l] = "+"
                j += 1
                l += 1
                q = 2
            elif Track_1[j] == "+" and Track_2[k] == "-" and Track_3[l] == "B":
                Track_3[l] = "-"
                j += 1
                l += 1
                q = 2
            elif Track_1[j] == "-" and Track_2[k] == "+" and Track_3[l] == "B":
                Track_3[l] = "-"
                j += 1
                l += 1
                q = 2
            elif Track_1[j] == 1 and Track_2[k] == "+" and Track_3[l] == "B":
                j -= 1
                k += 1
                q = 3
            elif Track_1[j] == 1 and Track_2[k] == "-" and Track_3[l] == "B":
                j -= 1
                k += 1
                q = 3
        # State q3
        elif q == 3:
            if Track_1[j] == "+" and Track_2[k] == "B" and Track_3[l] == "B":
                j -= 1
                q = 3
            elif Track_1[j] == "-" and Track_2[k] == "B" and Track_3[l] == "B":
                j -= 1
                q = 3
            elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
                j -= 1
                q = 3
            elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
                j += 1
                q = 0

    print("Track 1: ", end="")
    for i in range (len(Track_1)):
        print (Track_1[i], end="")

    print("\nTrack 2: ", end="")
    for i in range (len(Track_2)):
        print (Track_2[i], end="")

    print("\nTrack 3: ", end="")
    for i in range (len(Track_3)):
        print (Track_3[i], end="")

    a = Track_3.count("+")
    b = Track_3.count("-")

    if a > b:
        result = a
    elif a == b:
        result = 0
    else:
        result = -b
    
    if a > b:
        print("\nHasil: ", a, sep="")
    elif a == b:
        print("\nHasil: ", a, sep="")
    else:
        print("\nHasil: -", b, sep="")
        
    return Track_1, Track_2, Track_3, result