def program4258():
    n,m=input().split()
    n,m=int(n),int(m)
    lis=input().split()
    for i in range(len(lis)):
        lis[i]=int(lis[i])
    dic={}
    for i in range(1,n+1):
        dic[i]=[]
    for i in range(m):
        for j in range(lis[i],n+1):
            dic[j].append(lis[i])
    for i in range(1,n+1):
        print(dic[i][0],end=' ')