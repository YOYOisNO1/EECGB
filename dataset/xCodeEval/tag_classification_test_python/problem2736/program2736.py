def program2736():
    import math
    n=input()
    a=list(map(lambda x:int(x),input().split()))
    a_min=min(a)
    a_max=max(a)
    isFind=False
    ans=math.inf
    for i in range(a_min,a_max+1):
        diff=0
        flag=True
        for j in a:
            if j-i==0:
                continue
            else:
                if diff==0:
                    diff=abs(i-j)
                elif abs(j-i)!=diff:
                    flag=False
                    break
        if flag:
            ans=min(ans,diff)
            isFind=True
    if not isFind:
        print(-1)
    else:
        print(ans)