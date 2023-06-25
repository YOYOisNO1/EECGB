def func(n,a,b,ar,l):
        cost = 0
        d = {0:a,1:b}
        if((l+1)%2==1):
            if(ar[l//2]==2):
                cost=cost+min(a,b)
        for i in range((l+1)//2):
            if(ar[i]==ar[l]):
                if(ar[i]==2):
                    cost+=2*min(a,b)
            elif(ar[i]!=ar[l]):
                if((ar[i]==1 and ar[l]==0) or (ar[i]==0 and ar[l]==1)):
                    return(-1)
                elif(ar[i]==2):
                    cost=cost+d[ar[l]]
                elif(ar[l]==2):
                    cost=cost+d[ar[i]]
            l=l-1
        return(cost)
    
    n, a, b = map(int, input().split())
    ar = [int(i) for i in input().split()]
    l = len(ar)-1
    print(func(n,a,b,ar,l))
                
                