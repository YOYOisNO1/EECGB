def program3605():
    n, t = input().split()
    q = input() + "N"
    newQ = ""
    skip = 0
    
    for i in range(int(t)):
        for j in range(int(n)):
            if skip == 1:
                skip = 0
                continue
    
            if q[j] == "G" and q[j + 1] == "G":
                newQ += "G"
    
            elif q[j] == "G" and q[j + 1] == "B":
                newQ += "G"
    
            elif q[j] == "B" and q[j + 1] == "G":
                newQ += "GB"
                skip = 1
    
            elif q[j] == "B" and q[j + 1] == "B":
                newQ += "B"
            
            elif q[j] == "B" and q[j + 1] == "N":
                newQ += "B"
    
            elif q[j] == "G" and q[j + 1] == "N":
                newQ += "G"
    
        result = newQ
        q = newQ + "N"
        newQ = ""
    
    print(result)