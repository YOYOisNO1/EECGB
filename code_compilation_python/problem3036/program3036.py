def ayy(b1, b2):
        b1 = b1.replace("X","")
        b2 = b2.replace("X","")
        #moves string through cycle
        if b1 == b2:
            print("YES")
        elif b1[1:]+b1[0] == b2:
            print("YES")
        elif b1[2]+b1[:2] == b2:
            print("YES")
        else:
            print("NO")
    
def go():
        s = ""
        sentinel = '' # ends when this string is seen
        for line in iter(input, sentinel):
            s += (line + "\n")
        s = s[:len(s)-1]
        A = s.split("\n")
        b1 = A[0]+A[1][1]+A[1][0]
        b2 = A[2]+A[3][1]+A[3][0]
        #gets clockwise motion of the strings 
        ayy(b1,b2)
    
    go()
    
    