def program3285():
    input()
    l=0
    for x in map(int,input().split()):
        if x>l+15: break
        l=x
    print((min(l+15,90)))