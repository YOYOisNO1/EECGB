def program4651():
    import sys
    n,k=map(int,input().split())
    s=input()
    lp={}
    act=set()
    for i in range(n):
        lp[s[i]]=i
    for i in range(n):
        act.add(s[i])
        if len(act)>k:
            print("YES")
            sys.exit()
        elif lp[s[i]]==i:
            act.remove(s[i])
    print("NO")