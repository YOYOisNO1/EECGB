def program3973():
    n=int(input())
    k=int(input())
    for i in range(int(n/2),-1,-1):
        if i%(k+1)==0:
            d=i/(k+1)
            c=i-d
            if (d>=0 and c>=0):
                print(int(d),int(c),int(n-d-c))
                break
            