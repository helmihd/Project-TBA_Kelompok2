def subtraction(num1, num2):
    # Mendeklarasikan 2 track kosong
    Track_1 = []
    Track_2 = []

    # Meminta user memasukkan input bilangan pertama
    input_1 = num1

    # Meminta user memasukkan input bilangan kedua
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

    # Menambahkan blank di awal dan akhir di kedua track
    for i in range(abs(input_1) + abs(input_2) + 1):
        Track_1.insert(0, "B")
        Track_1.append("B")

    for i in range(abs(input_1) + abs(input_2)):
        Track_2.append("B")
        Track_2.append("B")
        Track_2.append("B")
    Track_2.append("B")
    Track_2.append("B")
    Track_2.append("B")

    j = abs(input_1) + abs(input_2) + 1
    k = abs(input_1) + abs(input_2) + 1
    # Initial State q0
    q = 0

    while q not in [3, 5, 6, 8, 10, 11]:
        # State q0
        if q == 0:
            if Track_1[j] == "+":
                Track_2[k] = Track_1[j]
                j += 1
                k += 1
                q = 0
            elif Track_1[j] == "-":
                Track_2[k] = Track_1[j]
                j += 1
                k += 1
                q = 0
            elif Track_1[j] == 1:
                j += 1
                k -= 1                
                q = 1
        # State q1
        elif q == 1:
            if Track_1[j] == "+" and Track_2[k] == "+":
                Track_2[k] = "B"
                j += 1
                k -= 1
                q = 2
            elif Track_1[j] == "+" and Track_2[k] == "B":
                Track_2[k] = "-"
                j += 1
                k -= 1
                q = 2
            elif Track_1[j] == "-" and Track_2[k] == "+":
                k += 1
                q = 4
            elif Track_1[j] == "+" and Track_2[k] == "-":
                k += 1
                q = 7
            elif Track_1[j] == "-" and Track_2[k] == "-":
                Track_2[k] = "B"
                j += 1
                k -= 1
                q = 9
            elif Track_1[j] == "-" and Track_2[k] == "+":
                Track_2[k] = "+"
                j += 1
                k -= 1
                q = 9
            elif Track_1[j] == "B":
                q = 11
        # State q2
        elif q == 2:
            if Track_1[j] == "+" and Track_2[k] == "+":
                Track_2[k] = "B"
                j += 1
                k -= 1
            elif Track_1[j] == "+" and Track_2[k] == "B":
                Track_2[k] = "-"
                j += 1
                k -= 1     
            elif Track_1[j] == "B" and Track_2[k] == "+":
                q = 3
            elif Track_1[j] == "B" and Track_2[k] == "B":
                q = 6
        # State q4
        elif q == 4:
            if Track_1[j] == "-" and Track_2[k] == "B":   
                Track_2[k] = "+"
                j += 1
                k += 1
            else:
                q = 5
        # State q7
        elif q == 7:
            if Track_1[j] == "+" and Track_2[k] == "B":
                Track_2[k] = "-"
                j += 1
                k += 1
            else:
                q = 8
        # State q9
        elif q == 9:
            if Track_1[j] == "-" and Track_2[k] == "-":
                Track_2[k] = "B"
                j += 1
                k -= 1
            if Track_1[j] == "-" and Track_2[k] == "B":
                Track_2[k] = "+"
                j += 1
                k -= 1
            elif Track_1[j] == "B":
                q = 10

    print("Track 1: ", end="")
    for i in range (len(Track_1)):
        print (Track_1[i], end="")

    print("\nTrack 2: ", end="")
    for i in range (len(Track_2)):
        print (Track_2[i], end="")

    a = Track_2.count("+")
    b = Track_2.count("-")

    if a > b:
        result = a
    elif a == b:
        result = 0
    else:
        result = -b
    
    return Track_1, Track_2, result
