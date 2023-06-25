def program4442():
    n=int(input())
    p=1
    for i in range(n):
        p*=2*i+1
        p%=1000000007
    print(p)