def program1693():
    n=int(input())
    if n==1:
        print(1)
        exit()
    p=[1]
    for i in xrange(1, n):
        p.append(1)
        if True:
            f=0
            if len(p)==1:
                break
            while p[len(p)-1]==p[len(p)-2]:
                p[len(p)-2]+=1
                del p[len(p)-1]
                if len(p)==1:
                    f=1
                    break
    for i in p:
        print(i,)
        
        