def program1336():
    s = input() 
    s = s + " " 
    if s[1]==' ': 
        M=int(s[0]) 
        if s[3]==' ': 
            N=int(s[2]) 
        else: 
            N=int(s[2]+s[3]) 
    else: 
        M=int(s[0]+s[1]) 
        if s[4]==' ':
            N=int(s[3]) 
        else: 
            N=int(s[3]+s[4]) 
    
    
    
    if M%2==0 or N%2==0: 
        a = int(M*N/2) 
    else: 
        a = int((M*N-1)/2) 
    
    print(a)