def program213():
    n=int(input())
    b=[]
    prime = [True for i in range(n+1)] 
    p=2
    while(p**2<=n):
        if prime[p] == True: 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n): 
        if prime[p]: 
            b.append(p)
    #print(*b)
    for i in b:
        if n%i==0:
            exit(print(n//i))
    print('1')
    