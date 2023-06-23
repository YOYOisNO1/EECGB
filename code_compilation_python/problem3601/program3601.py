def program3601():
    
    
    
    
    d = {"?": 10, "A":10, "B":10,"C": 10,"D":10,"E":10, "F":10,"G": 10,"H":10,"I":10, "J":10}
    
    lett = set(list("ABCDEFGHIJ"))
    
    for i in range(10):
        d[str(i)]=1
    
    print d
    
    k = set(d.keys())
    
    total = 1
    
    #with open("task1.txt", "r") as f:           
    #    for line in f:
    for line in sys.stdin:
        if line[0] == "?":
            total *= 9
        elif line[0] >= "A" and line[0] <= "J":
            total *= 9
            d[line[0]] = 1
            lett.remove(line[0])
            for m in lett:
                d[m] -= 1
            
            
        for c in line[1:]:       
            if c not in k:
                break
            total *= d[c]
            if c in lett:
                d[c] = 1
                lett.remove(c)
                for m in lett:
                    d[m] -= 1
        break
            
            
    print total
        
        
    
        
        