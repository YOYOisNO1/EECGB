def program2520():
    n=int(input())
    for i in range(n):
        m=int(input())
        j=1
        s=set()
        while j:
            if j*j<=m:
                s.add(j*j)
            else:
                break
            if j*j*j<=m:
                s.add(j*j*j)
            j+=1    
                
        print(len(s))