def program63():
    n,m=[int(x) for x in input().split()]
    a=set([int(x) for x in input().split()])
    b=set([int(x) for x in input().split()])
    c=list(a&b)
    if len(c)!=0:
        print(min(c))
    else:
        e=str(min(a))+str(min(b))
        print(min([int(e),int(e[::-1])]))