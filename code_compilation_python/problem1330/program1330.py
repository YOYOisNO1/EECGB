def program1330():
    n=int(input())
    p=list(map(int,input().split()))
    ka=list(map(int,input().split()))
    so=list(set(p))
    po=list(set(ka))
    tod=[]
    lol=[]
    sam=[]
    lil=[]
    loll=0
    tt=[]
    lkl=[]
    for item in so:
        tod.append(item)
    for item in po:
        if item not in tod:
            tod.append(item)
    for item in tod:
        lol.append(ka.count(item)+p.count(item))
    for item in lol:
        if item%2==0:
            pass
        else:
            loll=1
            break
    if loll=1:
        print(-1)
    else:
        for item in tod:
            sam.append(p.count(item))
            lol.append(ka.count(item))
        for x in range(n):
            if sam[x]=lol[x]:
                pass
            elif sam[x]>lol[x]:
                tt.append(((sam[x]+lol[x])//2)-lol[x])
            else:
                lkl.append(((sam[x]+lol[x])//2)-sam[x])
        if sum(tt)!=sum(lkl):
            print(-1)
        else:
            print(sum(tt)//2)
                
            
        