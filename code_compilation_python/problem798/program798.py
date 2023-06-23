def program798():
    comparação=0
    s=input("")
    t=input("")
    n=len(t)
    
    for i in range(0,n):
    
        if s[i] == t[n-i-1]:
            comparação+=1
       
         
    if comparação==n:
        print("YES")
        
    else:
        print("NO")