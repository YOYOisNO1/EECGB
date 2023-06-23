    import sys,math
def rec(now,numb,summ):
        if now<n:
            if z[now][numb]==2:
                rec(now+1,numb+1, summ/2)
                rec(now+1,numb, summ/2)
            else:
                z[now][numb]+=summ
                if z[now][numb]>2:
                    z[now][numb]=2
                    h=z[now][numb]-2
                    rec(now+1,numb+1, summ/2)
                    rec(now+1,numb, summ/2)
                    
            
    n,m=map(int,input().split())
    z=[]
    for i in range(1,n+1):
        z.append([0]*i)
    for i in range(1,m+1):
        rec(0,0,2)
    s=0
    for i in range(n):
        s+=z[i].count(2)
    print(s)