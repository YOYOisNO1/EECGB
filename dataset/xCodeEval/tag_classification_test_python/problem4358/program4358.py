def program4358():
    n,k=map(int,input().split())
    x=1
    m=100000000000000000000000000
    a=[0]*(k)
    for i in range(0,k):
        if(i==0 or n%i!=0):
            a[i]=m
        else:
            a[i]=(n//i)*k+i
    print(min(a))
        
        