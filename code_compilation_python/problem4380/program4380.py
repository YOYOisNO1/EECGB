def program4380():
    n = int(input())
    
    a,b = 0,0
    for i in range(n):
        if i%2==0:
            a+=b+1
        else
            b+=a+1
        a,b = a%1000000007,b%1000000007
    print((a+b)%1000000007)