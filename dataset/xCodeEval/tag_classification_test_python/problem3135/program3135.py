def program3135():
    n=int(input())
    k=pow(2,n)-2
    ans=pow(4,k,1000000007)
    print((ans*6)%1000000007)