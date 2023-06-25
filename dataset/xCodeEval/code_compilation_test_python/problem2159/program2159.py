def program2159():
    import itertools
    
    n,m=map(int,input().split())
    xlist=[int(x) for x in input().split()]
    segmentlist=[]
    segmentcolorlist=[0]*m
    for i in range(m):
        segmentlist.append(tuple(int(x) for x in input().split()))
    combpoints=set()
    new=False
    
    for i in range(n+1):
        red=i
        blue=n-i
        combpoints=combpoints | set(itertools.permutations('0'*red+'1'*blue,n))
    
    for combination in combpoints:
        new=False
        for i in range(m):
            for j in range(n):
                if segmentlist[i][0]<=xlist[j] and xlist[j]<=segmentlist[i][1]:
                    if combination[j]=='0':
                        segmentcolorlist[i]-=1
                    else:
                        segmentcolorlist[i]+=1
        for color in segmentcolorlist:
            if color+1 not in range(3):
                segmentcolorlist=[0]*m
                new=True
                break
        if new==False:
            print(''.join([str(combination[i])+' ' for i in range(n)]))
            break