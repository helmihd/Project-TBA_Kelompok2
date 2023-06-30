# Mendeklarasikan 2 track kosong
Track_1 = []
Track_2 = []
Track_3 = []

# Meminta user memasukkan input bilangan
input_1 = int(input("Masukkan bilangan pokok: "))


# Memasukkan input 1 ke Track 1
for i in range(abs(input_1)):
    Track_1.append(0)


# Menambahkan blank di awal dan akhir di semua track
for i in range(input_1 + 1):
    Track_1.append("B")
for i in range(input_1 + 1):
    Track_1.insert(0, "B")
Track_1.append("B")

for i in range(input_1):
    Track_2.append("B")
for i in range(input_1 + 1):
    Track_2.append("B")
    Track_2.insert(0, "B")
Track_2.append("B")

for i in range(input_1):
    Track_3.append("B")
for i in range(input_1 + 1):
    Track_3.append("B")
    Track_3.insert(0, "B")
Track_3.append("B")
    
j = input_1 + 1
k = input_1 + 1
l = input_1 + 1

# Initial State q0
q = 0

while q not in [9]:
    print("State: q", q)
    print("Track 1: ", end="")
    for i in range (len(Track_1)):
        print (Track_1[i], end="")
    print(": ", Track_1[j], end="")
    
    print("\nTrack 2: ", end="")
    for i in range (len(Track_2)):
        print (Track_2[i], end="")
    print(": ", Track_2[k], end="")
    
    print("\nTrack 3: ", end="")
    for i in range (len(Track_3)):
        print (Track_3[i], end="")
    print(": ", Track_3[l], end="")
    print("\n")

    # State q0
    if q == 0:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            j += 1
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            j -= 1
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = "B"
            j -= 1
            q = 2
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 8
    # State q2
    elif q == 2:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = "B"
            Track_2[k] = 0
            j -= 1
            k += 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            l -= 1
            q = 5

    # State q3
    elif q == 3:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            k -= 1
            l += 1
            q = 4
        elif Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            q = 1
    # State q4
    elif q == 4:
        if Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            Track_1[j] = 0
            Track_2[k] = "B"
            j += 1
            k -= 1
            q = 4
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            j -= 1
            q = 1

    # State q5
    elif q == 5:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            l += 1
            q = 8
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == 0:
            k -= 1
            l += 1
            q = 6
    # State q6
    elif q == 6:
        if Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            Track_2[k] = "B"
            l -= 1
            q = 7
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 9
    # State q9
    elif q == 9:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == 0:
            Track_3[l] = "B"
            l -= 1
            q = 7
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            l += 1
            q = 8
    # State q9
    elif q == 8:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "X"
            l += 1
            q = 9

print("Track 1: ", end="")
for i in range (len(Track_1)):
    print (Track_1[i], end="")

print("\nTrack 2: ", end="")
for i in range (len(Track_2)):
    print (Track_2[i], end="")

print("\nTrack 3: ", end="")
for i in range (len(Track_3)):
    print (Track_3[i], end="")

a = Track_3.count(0)

if a > 0:
    print("\nHasil: ", a, sep="")
else:
    print("\nHasil: Input Tidak Valid")
