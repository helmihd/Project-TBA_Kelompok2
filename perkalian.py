# Mendeklarasikan 2 track kosong
Track_1 = []
Track_2 = []
Track_3 = []

# Meminta user memasukkan input bilangan pertama
input_1 = int(input("Masukkan bilangan ke-1: "))

# Meminta user memasukkan input bilangan kedua
input_2 = int(input("Masukkan bilangan ke-2: "))

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

Track_1.append("B")

j = 0
k = 0
l = 0
# Initial State q0
q = 0

while q not in [4]:
    # State q0
    if q == 0:       
        if Track_1[j] == "+":
            Track_2.insert(k, Track_1[j])
            Track_3.insert(l, Track_2[k])
            j += 1
            k += 1
            q = 1
        elif Track_1[j] == "-":
            Track_2.insert(k, Track_1[j])
            Track_3.insert(l, Track_2[k])
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