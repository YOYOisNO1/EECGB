def program1543():
    p,d=map(int,input().split())
    p+=1
    ans=p
    i=10
    
    while i<1000000000000000001:
        if p%i<=d:
            ans=p-p%i
        i*=10
    print(ans-1)