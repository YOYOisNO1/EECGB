    import sys
    LI=lambda:list(map(int, sys.stdin.readline().split()))
    MI=lambda:map(int, sys.stdin.readline().split())
    SI=lambda:sys.stdin.readline().strip('\n')
    II=lambda:int(sys.stdin.readline())
    
    from math import log2
def fun(n, p, l, r):
        m=(l+r)//2
        if m==p:
            return n%2
        elif p>m:
            return fun(n//2, p, m+1, r)
        else:
            return fun(n//2, p, l, m-1)
    n, l, r=MI()
    if n==0:
        print(0)
        exit()
    e=2**(int(log2(n))+1)-1
    ans=0
    for i in range(l, r+1):
        if i%2:
            ans+=1
        else:
            ans+=fun(n, i, 1, e)
    print(ans)