def program367():
    a,b,c=map(int,input().split())
    z=list(map(int,input().split()))
    x=[]
    for i in range(b,len(z)):
        if z[i]!=0 and z[i]<=c:
            x.append((i-b+1)*10)
    for i in range(0,b-1):
        if z[i]!=0 and z[i]<=c:
            x.append((b-i-1)*10)
    print(min(x))