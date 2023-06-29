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

for i in range(abs(input_1) * abs(input_2)):
    Track_3.append("B")
    Track_3.append("B")
for i in range(abs(input_1) + abs(input_2) + 2):
    Track_3.append("B")
Track_3.append("B")

j = abs(input_1) * abs(input_2) + 1
k = abs(input_1) * abs(input_2) + 1
l = abs(input_1) * abs(input_2) + 1
# Initial State q0
q = 0

while q not in [7]:
    

print("Track 1: ", end="")
for i in range (len(Track_1)):
    print (Track_1[i], end="")

print("\nTrack 2: ", end="")
for i in range (len(Track_2)):
    print (Track_2[i], end="")

print("\nTrack 3: ", end="")
for i in range (len(Track_3)):
    print (Track_3[i], end="")
    