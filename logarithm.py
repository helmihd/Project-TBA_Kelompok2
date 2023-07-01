def logarithm (Track_1, Track_2, Track_3, q, j, k, l): 
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
    # State q7
    elif q == 7:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == 0:
            Track_3[l] = "B"
            l -= 1
            q = 7
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            l += 1
            q = 8
    # State q8
    elif q == 8:
        if Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = "X"
            l += 1
            q = 9

    
    return Track_1, Track_2, Track_3, q, j, k, l
