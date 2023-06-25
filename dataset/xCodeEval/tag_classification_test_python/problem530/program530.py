def program530():
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    #print((l))
    if x==0:
        if 0 in l:
            print((1))
        else:
            print((0))
    else:
        c=0
        if x in l:
            c=1
        x=x-1    
        while x!=-1:
            if x not in l:
                c+=1
            x-=1    
            
        print((c))    
            