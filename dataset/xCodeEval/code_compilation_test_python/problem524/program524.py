def program524():
    r,c=map(int,input().split())
    co=0
    lis=[]
    for i in range(r):
        st=input()
        for i in range(c):
            if st[i]=="S":
                lis.append(i)
        for i in range(c):
            if st[i]=="S":
                co+=1
                break
    if len(lis)>0:
        lis=set(lis)
    print((r*c)-(len(lis)*co)