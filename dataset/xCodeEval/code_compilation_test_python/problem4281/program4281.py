    n,m=list(map(int, input().split() ) )
    s1=list(map(int, input().split() ) )
    s2=list(map(int, input().split() ) )
    p1=[]
    p2=[]
    for i in range(n):
        p1.append([s1[i*2], s1[i*2+1] ])
    for i in range(m):
        p2.append([s2[i*2], s2[i*2+1] ])
def check(pair1, pair2):
        a1,b1=pair1[0], pair1[1]
        a2,b2=pair2[0], pair2[1]
        if a1==a2 and b1!=b2 or a1==b2 and a2!=b1 or b1==a2 and a1!=b2 or b1==b2 and a1!=a2:
            return True
        else:
            return False
    c1=[]
    c2=[]
    for i in range(n):
        add=[]
        for j in range(m):
            if check(p1[i], p2[j]):
                add.append(j)
        c1.append(add)
    for i in range(m):
        add=[]
        for j in range(n):
            if check(p2[i], p1[j]):
                add.append(j)
        c2.append(add)
    maxlen1=0
    maxlen2=0
    for i in c1:
        if len(i)>maxlen1:
            maxlen1=len(i)
            pair1=i[0]
    for i in c2:
        if len(i)>maxlen2:
            maxlen2=len(i)
            pair2=i[0]
    if maxlen1>=2 or maxlen2>=2:
        print(-1)
    else:
        count=0
        for i in c1:
            if len(i)!=0:
                count+=1
        if count==1:
            p1=p1[pair1]
            p2=p2[pair2]
            if p1[0]==p2[0] or p1[0]==p2[1]:
                t=p1[0]
            else:
                t=p1[1]
            print(t)
        else:
            print(0)
            