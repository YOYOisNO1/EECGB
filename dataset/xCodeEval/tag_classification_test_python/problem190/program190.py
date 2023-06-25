def program190():
    t=int(input())
    l=[]
    s=0
    for i in range(t):
        l.append(tuple(map(int,input().split())))
    for i in range(t-1):
        for j in range(i+1,t):
            if l[i][0]==l[j][1]:
                s+=1
            if l[i][1]==l[j][0]:
                s+=1
    print(s)