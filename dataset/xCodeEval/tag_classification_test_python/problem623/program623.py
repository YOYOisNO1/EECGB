def program623():
    normal=[31,28,31,30,31,30,31,31,30,31,30,31]
    leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    poss=[normal+normal+normal,normal+normal+leap,normal+leap+normal,leap+normal+normal]
    n=int(input())
    m=map(int,input().split())
    y=False
    for p in poss:
        for i in xrange(len(p)-n+1):
            poss=True
            for j in xrange(n):
                if p[i+j]!=m[j]:
                    poss=False
                    break
            if poss:
                y=True
                break
    print('Yes') if y else 'No'
        