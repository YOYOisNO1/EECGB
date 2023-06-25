def program3763():
    n=int(input())
    l=[int(x) for x in input().split()]
    if n==1:
        if l[0]==15:
            print("DOWN")
        elif l[0]==0:
            print("UP")
        else:
            print("-1")
    elif l[n-1]>l[n-2] and l[n-1]!=15:
        print("UP")
    else:
        if l[n-1]==0:
            print("UP")
        else:
            print("DOWN")