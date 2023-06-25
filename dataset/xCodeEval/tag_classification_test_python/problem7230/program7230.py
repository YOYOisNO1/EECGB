def program7230():
    l=input().split()
    for i in range(len(l)):
        l[i]=int(l[i])
    p1=int(l[0])
    p2=int(l[1])
    p3=int(l[2])
    p4=int(l[3])
    start=int(l[4])
    end=int(l[5])
    q=int(0)
    for j in range(start,end+1):
        if int((((j%p1)%p2)%p3)%p4)==j:
            q+=1
    print(int(q))