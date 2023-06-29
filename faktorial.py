# Mendeklarasikan 2 track kosong
Track_1 = []
Track_2 = []
Track_3 = []

# Meminta user memasukkan input bilangan
input_1 = int(input("Masukkan bilangan yang ingin difaktorial: "))

# Memberi pembatas
Track_1.append(1)

# Memasukkan input ke Track 1
for i in range(abs(input_1)):
    Track_1.append(0)
    
# Menambahkan blank di awal dan akhir di semua track
for i in range(abs(input_1) + 1):
    Track_1.insert(0, "B")
    Track_1.append("B")
    
for i in range(abs(input_1)):
    Track_2.append("B")
    Track_2.append("B")
for i in range(abs(input_1) + 2):
    Track_2.append("B")
    Track_2.append("B")

for i in range(abs(input_1)):
    Track_3.append("B")
    Track_3.append("B")
for i in range(abs(input_1) + 2):
    Track_3.append("B")
    Track_3.append("B")

j = abs(input_1) + 1
k = abs(input_1) + 1
l = abs(input_1) + 1
# Initial State q0
q = 0

while q not in [5, 6]:
    # State q0
    if q == 0:       
        if Track_1[j] == 0:
            Track_2[k] = Track_1[j]
            j += 1
            k += 1
            q = 0
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = "X"
            j -= 1
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = 1
            j -= 1
            k -= 1
            q = 2
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            q = 5
    # State q2
    elif q == 2:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_3[l] = 0
            j -= 1
            l += 1
            q = 2
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            q = 2
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            j += 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 3
        elif Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = 1
            k += 1
            l -= 1
            q = 4
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            q = 5
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            q = 6
    # State q3
    elif q == 3:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            j += 1
            q = 3
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 3
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_2[k] = "B"
            j -= 1
            k -= 1
            q = 2
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == 0:
            Track_2[k] = "B"
            j -= 1
            k -= 1
            q = 2
    # State q4
    elif q == 4:
        if Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == 0:
            Track_2[k] = 0
            k += 1
            l -= 1
            q = 4
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            j -= 1
            k -= 1
            q = 2


print("Track 1: ", end="")
for i in range (len(Track_1)):
    print (Track_1[i], end="")

print("\nTrack 2: ", end="")
for i in range (len(Track_2)):
    print (Track_2[i], end="")

print("\nTrack 3: ", end="")
for i in range (len(Track_3)):
    print (Track_3[i], end="")

