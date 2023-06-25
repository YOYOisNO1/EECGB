def program1247():
    a=[0]*100001
    k=int(input())
    l=int(input())
    m=int(input())
    n=int(input())
    d=int(input())
    for i in range(k,d+1,k):
        a[i]=1
    
    for i in range(l,d+1,l):
        a[i]=1
    
    for i in range(m,d+1,m):
        a[i]=1
    
    for i in range(n,d+1,n):
        a[i]=1
    print(a.count(1))
    
        