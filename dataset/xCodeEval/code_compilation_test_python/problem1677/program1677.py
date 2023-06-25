def program1677():
    n=input()
    l=input().split()
    l=map(x : int(x),l)
    l=sorted(l)
    s=set()
    su=0
    for i in l[::-1]:
        q=True
        for j in xrange(i, 0, -1):
            if not j in s and q:
                su+=j
                s.insert(j)
                q=False
    print su