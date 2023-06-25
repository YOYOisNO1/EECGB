def program4170():
    n=input()
    lst=map(int,input().split())
    from collections import *
    v=Counter(lst)
    #print v
    ans=0
    s=list(set(lst))
    i=0
    s.sort()
    i=2
    dp=[]
    for i in v:
        dp.append((v[i],i))
    dp.sort(reverse=True)
    from heapq import *
    
    h=[]
    heapify(h)
    for i in range(0,len(dp)):
        heappush(h,[-dp[i][0],dp[i][1]])
    if len(s)<=2:
        print 0
    else:
        i=2
    
        pe=[s[0],s[1]]
        fv=[]
        while len(h)>2:
            t1=heappop(h)
            t2=heappop(h)
            t3=heappop(h)
            if t1[0]<0 and t2[0]<0 and t3[0]<0:
                t1[0]=t1[0]+1
                t2[0]=t2[0]+1
                t3[0]=t3[0]+1
                fv.append((t1[1],t2[1],t3[1]))
            if t1[0]!=0:
                heappush(h,t1)
            if t2[0]!=0:
                heappush(h,t2)
            if t3[0]!=0:
                heappush(h,t3)
    
        if len(fv)==0:
            print 0
        else:
            print len(fv)
            for i in fv:
    
                tu=[i[0],i[1],i[2]]
                tu.sort()
                print tu[2],tu[1],tu[0]