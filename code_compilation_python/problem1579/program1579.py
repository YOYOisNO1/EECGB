def program1579():
    n=int(input())
    a=[int(i) for i in input().split()] 
    k=True
    m=0
    i=0
    while k and i<n-1:
        if (a[i]==1 and a[i+1]==3) or (a[i]==3 and a[i+1]==1):
            m+=4
        elif (a[i]==1 and a[i+1]==2) or (a[i]==2 and a[i+1]==1):
            m+=3
        else:
            k=False
    if k:
        print("Finite")
        print(m)
    else:
        print("Infinite") 