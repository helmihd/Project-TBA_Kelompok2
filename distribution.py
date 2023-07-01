def distribution (Track_1, Track_2, Track_3, q, j, k, l):
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
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_2[k] = 1
            j += 1
            k -= 1
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == "+" and Track_2[k] == "+" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 2
        elif Track_1[j] == "-" and Track_2[k] == "-" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 2
        elif Track_1[j] == "-" and Track_2[k] == "+" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 5
        elif Track_1[j] == "+" and Track_2[k] == "-" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 5
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 8
    # State q2
    elif q == 2:
        if Track_1[j] == "-" and Track_2[k] == "-" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 2
        elif Track_1[j] == "+" and Track_2[k] == "+" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 2
        elif Track_1[j] == "-" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "+"
            k += 1
            l += 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "+"
            k += 1
            l += 1
            q = 3
        elif Track_1[j] == "+" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "+"
            k += 1
            l += 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == "+" and Track_3[l] == "B":
            q = 4
        elif Track_1[j] == "B" and Track_2[k] == "-" and Track_3[l] == "B":
            q = 4
    # State q3
    elif q == 3:
        if Track_1[j] == "B" and Track_2[k] == "-" and Track_3[l] == "B":
            k += 1
            q = 3
        elif Track_1[j] == "-" and Track_2[k] == "-" and Track_3[l] == "B":
            k += 1
            q = 3
        elif Track_1[j] == "+" and Track_2[k] == "+" and Track_3[l] == "B":
            k += 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == "+" and Track_3[l] == "B":
            k += 1
            q = 3
        elif Track_1[j] == "+" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 2
        elif Track_1[j] == "B" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 2
        elif Track_1[j] == "-" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 2
    # State q5
    elif q == 5:
        if Track_1[j] == "-" and Track_2[k] == "+" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 5
        elif Track_1[j] == "+" and Track_2[k] == "-" and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            k -= 1
            q = 5
        elif Track_1[j] == "-" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "-"
            k += 1
            l += 1
            q = 6
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "-"
            k += 1
            l += 1
            q = 6
        elif Track_1[j] == "+" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "-"
            k += 1
            l += 1
            q = 6
        elif Track_1[j] == "B" and Track_2[k] == "+" and Track_3[l] == "B":
            q = 7
        elif Track_1[j] == "B" and Track_2[k] == "-" and Track_3[l] == "B":
            q = 7
    # State q6
    elif q == 6:
        if Track_1[j] == "B" and Track_2[k] == "-" and Track_3[l] == "B":
            k += 1
            q = 6
        elif Track_1[j] == "+" and Track_2[k] == "-" and Track_3[l] == "B":
            k += 1
            q = 6
        elif Track_1[j] == "-" and Track_2[k] == "+" and Track_3[l] == "B":
            k += 1
            q = 6
        elif Track_1[j] == "B" and Track_2[k] == "+" and Track_3[l] == "B":
            k += 1
            q = 6
        elif Track_1[j] == "-" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 5
        elif Track_1[j] == "+" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 5
        elif Track_1[j] == "B" and Track_2[k] == 1 and Track_3[l] == "B":
            k -= 1
            q = 5

    return Track_1, Track_2, Track_3, q, j, k, l