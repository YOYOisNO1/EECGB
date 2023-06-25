    from itertools import combinations
def substr(inp):
        return (''.join(s) for r in range(1,len(inp) + 1) for s in combinations(inp, r))
    
    temp=[]
    for i in xrange(45000):
        temp.append(i*i)
    
    s=input()
    p=list(set(substr(s)))
    le=len(p)
    for i in xrange(le):
        p[i]=int(p[i])
        if(p[i]==0):
            p[i]=-1
    p=sorted(p)
    
    for i in xrange(le):
        p[i]=str(p[i])
    #print(p)
    flag=0
    for i in xrange(le-1,-1,-1):
        if int(p[i]) in temp:
            print(len(s)-len(p[i]))
            flag=1
            break
    if flag==0:
        print(-1)