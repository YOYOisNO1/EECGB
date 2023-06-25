def program2365():
    n,w = map(int, input().split())
    a = [(-aa,i) for i,aa in enumerate(map(int,input().split()))]
    a.sort()
    a = [(-aa,i) for aa,i in a]
    #print("a",a)
    
    
    
    b = [[(aa+1)//2,i] for aa, i in a]
    #print("b",b)
    
    s = sum([aa for aa,i in b])
    if (s>w) :
        print(-1)
        exit()
    else:
        w-=s
    
    
    while(w>0) :
        c = False
        for i in range(n):
            if b[i][0] < a[i][0]:
                c = True
                b[i][0]+=1
                w-=1
                if w==0:
                    break
        if (c == False):
            break
    
    if (w!=0):
        print(-1)
        exit()
    
    #print("b",b)
    
    c = [(i,bb) for bb,i in b]
    #print("c",c)
    c.sort()
    #print("c",c)
    
    d = [str(bb) for i,bb in c]
    
    print(" ".join(d))
    