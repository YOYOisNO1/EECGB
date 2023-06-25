def program749():
    l1 = [int(x) for x in input().split()]
    c,v0,v1,a,l=l1[0],l1[1],l1[2],l1[3],l1[4]
    i=0
    days=0
    while i<c:
        days+=1
        today = max(0,-l*(int(days>1))+min(v0+a*(days-1),v1))
        i+=today
        
    print(days)