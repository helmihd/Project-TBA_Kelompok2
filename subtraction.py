def subtraction(Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k):
    # State q0
    if q == 0:
        if Track_1[j] == "+":
            Track_2[k] = Track_1[j]
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            q = 0
        elif Track_1[j] == "-":
            Track_2[k] = Track_1[j]
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            q = 0
        elif Track_1[j] == 1:
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"
                
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == "+" and Track_2[k] == "+":
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 2
        elif Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = "-"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 2
        elif Track_1[j] == "-" and Track_2[k] == "+":
            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            q = 4
        elif Track_1[j] == "+" and Track_2[k] == "-":
            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

            q = 7
        elif Track_1[j] == "-" and Track_2[k] == "-":
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 9
        elif Track_1[j] == "-" and Track_2[k] == "B":
            Track_2[k] = "+"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

            q = 9
        elif Track_1[j] == "B":
            q = 11
    # State q2
    elif q == 2:
        if Track_1[j] == "+" and Track_2[k] == "+":
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

        elif Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = "-"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"
     
        elif Track_1[j] == "B" and Track_2[k] == "+":
            q = 3
        elif Track_1[j] == "B" and Track_2[k] == "B":
            q = 6
    # State q4
    elif q == 4:
        if Track_1[j] == "-" and Track_2[k] == "B":   
            Track_2[k] = "+"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

        else:
            q = 5
    # State q7
    elif q == 7:
        if Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = "-"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k += 1
            Track_2_arrow[k] = "^"

        else:
            q = 8
    # State q9
    elif q == 9:
        if Track_1[j] == "-" and Track_2[k] == "-":
            Track_2[k] = "B"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

        if Track_1[j] == "-" and Track_2[k] == "B":
            Track_2[k] = "+"
            
            Track_1_arrow[j] = " "
            j += 1
            Track_1_arrow[j] = "^"

            Track_2_arrow[k] = " "
            k -= 1
            Track_2_arrow[k] = "^"

        elif Track_1[j] == "B":
            q = 10
    
    return Track_1, Track_1_arrow, Track_2, Track_2_arrow, q, j, k