def program1630():
    l=list(map(str,input().strip()))
    l.sort(reverse=True)
    n=l.count(l[0])
    print(l[0]*n)