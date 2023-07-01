def power (Track_1, Track_2, Track_3, q, j, k, l):
    # State q0
    if q == 0:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_2[k] = Track_1[j]
            j += 1
            k += 1
            q = 0
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            j += 1
            k -= 1
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_1[j] = "X"
            j += 1
            q = 2
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            Track_3[l] = 0
            k += 1
            l += 1
            q = 11
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 12
    # State q2
    elif q == 2:
        if Track_1[j] == "X" and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 2
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            Track_1[j] = "X"
            j -= 1
            q = 3
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_1[j] = "X"
            j -= 1
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == 0:
            q = 10
    # State q3
    elif q == 3:
        if Track_1[j] == "X" and Track_2[k] == 0 and Track_3[l] == "B":
            j -= 1
            q = 3
        elif Track_1[j] == "X" and Track_2[k] == 0 and Track_3[l] == 0:
            j -= 1
            q = 3
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == 0:
            j -= 1
            q = 4
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == "B":
            j -= 1
            q = 4
    # State q4
    elif q == 4:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_3[l] = 0
            j -= 1
            l += 1
            q = 4
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            j -= 1
            l += 1
            q = 4
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            j += 1
            q = 5
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 5
        elif Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            k += 1
            l -= 1
            q = 6
    # State q5
    elif q == 5:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            j += 1
            q = 5
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 5
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_2[k] = "B"
            j -= 1
            k -= 1
            q = 4
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == 0:
            Track_2[k] = "B"
            Track_3[l] = 0
            j -= 1
            k -= 1
            q = 4
    # State q6
    elif q == 6:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == 0:
            Track_2[k] = 0
            k += 1
            l -= 1
            q = 6
        elif Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            j += 1
            k -= 1
            l += 1
            q = 7
    # State q7
    elif q == 7:
        if Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == 0:
            j += 1
            q = 2
    # State q8
    elif q == 8:
        if Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            Track_3[l] = 0
            k -= 1
            l += 1
            q = 8
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 9
    # State q11
    elif q == 11:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            q = 12

    return Track_1, Track_2, Track_3, q, j, k, l