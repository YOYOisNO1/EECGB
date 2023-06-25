def program927():
    from bisect import *
    n,m=map(int,input().split())
    r=[0]*n
    q=[]
    for i in range(m):
        s,d,c=map(int,input().split())
        r[d-1]=m+1
        q.append([d-1,s-1,c,i+1])
    q.sort()
    for i1 in q:
        d,s,c,i=i1[0],i1[1],i1[2],i1[3]
        while (c):
            if (r[s]==0):
                r[s]=i
                c-=1
            if(s==d):
                print(-1)
                exit(0)
            s+=1
    print(*r)
                