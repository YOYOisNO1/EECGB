def program4100():
    n=input().split()
    l=int(n[0])
    r=int(n[1])
    s=0
    for i in range(l,r):
        i=str(i)
        if i[0]==i[len(i)-1]:
            s+=1
    print(s)        