def program2157():
    n,m=[int(x) for x in input().split()]
    points=[int(x) for x in input().split()]
    segments=[]
    colors = [None]*len(points)
    balances = [0]*len(segments)
    for i in range(m):
        a,b=[int(x) for x in input().split()]
        segments.append(a,b))
    segments.sort(key=lambda x: x[0])
    for for i in range(len(points)):
        p=points[i]
        b=[]
        b2=[]
        for j in range(len(segments)):
            if p>=segments[i][0] and p<=segments[i][1]:
                b.append(balances[i])
                b2.append(i)
        if 1 in b:
            colors[i]=1
            for i in b2:
                balances[i]=balances[i]-1
        elif -1 in b:
            colors[i]=0
            for i in b2:
                balances[i]=balances[i]+1
        else:
            colors[i]=1
            for i in b2:
                balances[i]=balances[i]-1
    print ' '.join(colors)