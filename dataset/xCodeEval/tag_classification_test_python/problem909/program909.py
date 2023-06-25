def program909():
    import sys
    
    
    s = input()
    n = len(s)
    
    yes = 0
    
    for i in range(n):
        t = s[i]
        t = int(t)
    
        if t%8 == 0:
            print('YES')
            print(t)
            yes = 1
            break
        
        for j in range(i+1, n):
    
            t = s[i]+s[j]
            t = int(t)
    
            if t%8 == 0:
                print('YES')
                print(t)
                yes = 1
                break
            
            for k in range(j+1, n):
    
                t = s[i]+s[j]+s[k]
                t = int(t)
    
                if t%8 == 0:
                    print("YES")
                    print(t)
                    yes = 1
                    break
    
            if yes:
                break
        if yes:
            break
    
    if not yes:
        print('NO')
    
    
    
        
    