def program2576():
    n=input()
    s=input()
    c,i = 0,0
    
    for i in range(n):
    
        path = 0
    
        if s[i] == 'U':
            path += 1
        elif s[i] == 'D':
            path += -1
        elif s[i] == 'R':
            path += +2
        elif s[i] == 'L':
            path += -2
    
        for j in range(i+1, n):
    
            if s[j] == 'U':
                path += 1
            elif s[j] == 'D':
                path += -1
            elif s[j] == 'R':
                path += +2
            elif s[j] == 'L':
                path += -2
    
            if path == 0:
                c += 1
               # break
    
         
    print c
            