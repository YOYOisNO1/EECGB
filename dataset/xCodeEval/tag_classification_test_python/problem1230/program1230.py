def program1230():
    n=input()
    a=map(int,input().split())
    x=max(a)
    print(x,)
    z=[]
    y=[]
    for i in a:
        if x%i==0:
            if i not in z:
                z.append(i)
            else:
                y.append(i)
        else:
            y.append(i)
    print(max(y))