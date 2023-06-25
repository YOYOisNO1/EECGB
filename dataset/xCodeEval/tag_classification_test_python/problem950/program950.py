def program950():
    import sys
    from itertools import permutations
    n=int(input())
    input=sys.stdin.readline
    r1,s1,p1=map(int,input().split())
    r2,s2,p2=map(int,input().split())
    a1=min(r1,s2)+min(s1,p2)+min(p1,r2)
    li=[[0,3],[0,5],[1,4],[1,3],[2,5],[2,4]]
    xx=list(permutations(li))
    a2=[]
    for i in xx:
        tem=[r1,s1,p1,r2,s2,p2]
        ans=0
        for j in i:
            pp=min(tem[j[0]],tem[j[1]])
            ans+=pp
            tem[j[0]]-=pp
            tem[j[1]]-=pp
        a2.append(ans)
    print(n-max(a2),a1)