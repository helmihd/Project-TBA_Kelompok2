def multiplication(Track_1, Track_2, Track_3, q, j, k, l):
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

    return Track_1, Track_2, Track_3, q, j, k, l