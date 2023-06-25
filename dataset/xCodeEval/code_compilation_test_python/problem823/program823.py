def program823():
    n, a, b = map(lambda x: int(x),str(input()).split())
    isa = map(lambda x:int(x),str(input())
    ans = ""
    for i in range(1, n+1):
        if i in isa:
            print '1'
        else:
            print '0'