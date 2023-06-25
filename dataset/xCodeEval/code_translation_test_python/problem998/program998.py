def program998():
    from sys import stdin
    b=int(stdin.readline().strip())
    g=int(stdin.readline().strip())
    n=int(stdin.readline().strip())
    st=set()
    ans=0
    for i in range(b+1):
        for j in range(g+1):
            if j+i==n:
                ans+=1
                
    
            
    print(ans)