def program1860():
    a,b=map(int,input().split())
    m=[0]*a
    m1=[]
    for i in range(b):
        m1.append(list(map(int,input().split())))
        m[m1[-1][1]-1]=b+1
        m1[-1].append(i+1)
    m1.sort(key = lambda x:x[1]-x[0])
    for i in m1:
        c=i[2]
        for j in range(i[0]-1,i[1]+1):
            if m[j] == 0:
                m[j]=i[3]
                c-=1
            if c == 0:
                break
        if c != 0:
            m1.sort()
            m=[0]*a
            for i in m1:
                m[i[1]-1] = b+1
            for i in m1:
                c=i[2]
                for j in range(i[0]-1,i[1]+1):
                    if m[j] == 0:
                        m[j]=i[3]
                        c-=1
                    if c == 0:
                        break
                if c != 0:
                    m=False
                    break
            break
    if m == False:
        print(-1)
    else:
        print(*m)