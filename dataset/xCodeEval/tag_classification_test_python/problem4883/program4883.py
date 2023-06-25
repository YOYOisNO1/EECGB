def program4883():
    n,k=map(int,input().split())
    a=[]
    b=[]
    import math
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            a.append(i)
            if i*i!=n:
                a.append(n//i)
    a.sort()
    
    if len(a)>=k:
        print(a[k-1])
    else:
        print(-1)