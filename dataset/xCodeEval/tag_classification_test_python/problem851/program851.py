def program851():
    n,m=[int(n) for n in input().split()]
    arr=[int(item) for item in input().split()]
    brr=[int(item) for item in input().split()]
    crr=[False]*10
    drr=[]
    for j in brr:
        crr[j]=True
    for i in arr:
        if(crr[i]==True):
            drr.append(i)
    print(*drr)        
        
                    
        