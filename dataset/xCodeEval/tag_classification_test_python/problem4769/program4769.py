def program4769():
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    sa=sum(a)
    sb=sum(b)
    if sa>=sb:
        print("Yes")
    else:
        print("No")