def program16():
    
    M = 998244353 
    n=int(input())
    a,b=1,1
    for i in range(n-1):a,b=b,a+b
    print(a*pow(1<<n,M-2,M)%M)