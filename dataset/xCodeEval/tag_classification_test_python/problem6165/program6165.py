def program6165():
    a,b,c,d=map(int,input().split())
    k=[]
    if a==c or b==d:
        k.append("1")
    else:
        k.append("2")
    x=a%2
    y=b%2
    z=c%2
    w=d%2
    if (x==y and z==w) or (x!=y and z!=w):
        if abs(a-c)==abs(d-b):
            k.append("1")
        else:    
            k.append("2")
    else:
        k.append("0")
    k.append(str(max(abs(d-b),abs(a-c))))
    print(" ".join(k))