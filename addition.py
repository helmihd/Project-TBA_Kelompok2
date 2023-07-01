def addition(Track_1, Track_2, q, j, k):
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
        elif Track_1[j] == 1:        
            j += 1
            k -= 1
            q = 1
    # State q1
    elif q == 1:
        if Track_1[j] == "+" and Track_2[k] == "+":     
            k += 1
            q = 2
        elif Track_1[j] == "-" and Track_2[k] == "+":
            Track_2[k] = "B"
            j += 1
            k -= 1           
            q = 4
        elif Track_1[j] == "-" and Track_2[k] == "B":
            Track_2[k] = Track_1[j]         
            j += 1        
            k -= 1            
            q = 4
        elif Track_1[j] == "+" and Track_2[k] == "-":
            Track_2[k] = "B"  
            j += 1
            k -= 1        
            q = 6
        elif Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = "+"     
            j += 1
            k -= 1       
            q = 6
        elif Track_1[j] == "-" and Track_2[k] == "-":
            k += 1
            q = 8
        elif Track_1[j] == "B":
            q = 10
    # State q2
    elif q == 2:
        if Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = Track_1[j]      
            j += 1   
            k += 1
        else:
            q = 3
    # State q4
    elif q == 4:
        if Track_1[j] == "-" and Track_2[k] == "+":
            Track_2[k] = "B"
            j += 1
            k -= 1
        elif Track_1[j] == "-" and Track_2[k] == "B":
            Track_2[k] = Track_1[j]       
            j += 1
            k -= 1
        else:
            q = 5
    # State q6
    elif q == 6:
        if Track_1[j] == "+" and Track_2[k] == "-":
            Track_2[k] = "B"
            j += 1        
            k -= 1     
        elif Track_1[j] == "+" and Track_2[k] == "B":
            Track_2[k] = Track_1[j]
            j += 1
            k -= 1
        else:
            q = 7
    # State q8
    elif q == 8:
        if Track_1[j] == "-" and Track_2[k] == "B":
            Track_2[k] = Track_1[j]
            j += 1
            k += 1
        else:
            q = 9
            
    return Track_1, Track_2, q, j, k