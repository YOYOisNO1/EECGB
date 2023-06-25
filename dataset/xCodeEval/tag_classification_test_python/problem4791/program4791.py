def program4791():
    n,m=map(int,input().split())
    c=[]
    a=[0]*n
    b=[0]*m
     
     
    for i in range(n):
            c.append(input())
     
    for i in range(n):
        for j in range(m):
            if c[i][j]=='.':
                b[j]+=1
                a[i]+=1
    d=m*a.count(m)
     
    d+=n*b.count(n)
    d=d-a.count(m)*b.count(n)
    print(d)