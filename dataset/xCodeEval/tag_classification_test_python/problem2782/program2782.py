def program2782():
    n=int(input())
    a=list(map(int,input().split(" ")))
    m=[]
    s=0
    f=0
    t=0
    for i in range(n):
        if a[i]==0:
            t+=1
        else:
            m.append([f,t])
            s=0
            f=i+1
            t=i+1
    if f!=i+1 and len(m)!=0:
        m[len(m)-1][1]=i
    if len(m)==0:
        print('NO')
    else:
        print('YES')
        print(len(m))
        for el in m:
            print(el[0]+1,el[1]+1)