def program4365():
    # Why do we fall ? So we can learn to pick ourselves up.
    x,y,l,r = map(int,input().split())
    ll = []
    for i in range(0,75):
        for j in range(0,75):
            if l <= pow(x,i)+pow(y,j) <= r:
                ll.append(pow(x,i)+pow(y,j))
    ll = sorted(set(ll))
    maxx = -1
    if len(ll) == 0:
        print(r-l+1)
    else:
        maxx = max(maxx,ll[0]-l)
        for i in range(1,len(ll)):
            maxx = max(ll[i]-ll[i-1]-1,maxx)
        maxx = max(maxx,r-ll[-1])
        print(maxx)
    