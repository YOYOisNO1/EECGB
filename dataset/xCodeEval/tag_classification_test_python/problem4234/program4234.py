def program4234():
    n=int(input())
    a=-1
    
    for i in range(1,n+1):
        if n%i==0 and n/i<n and n*i>n:
            a=i
            break
    if a!=-1:
        print(n,a)
    else:
        print(-1)
                
    