def factorial (Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l):
    # State q0
    if q == 0:       
        if Track_1[j] == 0:
            Track_2[k] = Track_1[j]
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            q = 0
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = "X"
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"

            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = 1
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 2
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            q = 5
    # State q2
    elif q == 2:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_3[l] = 0
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"

            Track_3_arrow[l] = " "
            l += 1
            Track_3_arrow[l] = "^"

            q = 2
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"
            
            Track_3_arrow[l] = " "
            l += 1
            Track_3_arrow[l] = "^"

            q = 2
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == "B":
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            q = 3
        elif Track_1[j] == "B" and Track_2[k] == 0 and Track_3[l] == 0:
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            q = 3
        elif Track_1[j] == 0 and Track_2[k] == "B" and Track_3[l] == "B":
            Track_1[j] = 1
            
            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"
            
            Track_3_arrow[l] = " "
            l -= 1
            Track_3_arrow[l] = "^"

            q = 4
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == 0:
            q = 5
        elif Track_1[j] == "B" and Track_2[k] == "B" and Track_3[l] == "B":
            Track_3[l] = 0
            q = 6
    # State q3
    elif q == 3:
        if Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == "B":
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            q = 3
        elif Track_1[j] == 0 and Track_2[k] == 0 and Track_3[l] == 0:
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            q = 3
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == "B":
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 2
        elif Track_1[j] == 1 and Track_2[k] == 0 and Track_3[l] == 0:
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"
            
            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 2
    # State q4
    elif q == 4:
        if Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == 0:
            Track_2[k] = 0
            
            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            Track_3_arrow[l] = " "
            l -= 1
            Track_3_arrow[l] = "^"

            q = 4
        elif Track_1[j] == 1 and Track_2[k] == "B" and Track_3[l] == "B":
            
            Track_1_arrow[j] = " "
            j -= 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            Track_3_arrow[l] = " "
            l += 1
            Track_3_arrow[l] = "^"

            q = 2
            
    return Track_1, Track_1_arrow, Track_2, Track_2_arrow, Track_3, Track_3_arrow, q, j, k, l