def program891():
    n,k=input().split()
    
    n=int(n)
    k=int(k)
    for i in range(0,k):
            if(n%10==0):
                    n=n/10
            else:
                    n=n-1
    print(n)