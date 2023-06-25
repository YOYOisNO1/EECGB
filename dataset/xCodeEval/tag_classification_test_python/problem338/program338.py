def program338():
    import math
    #q=int(input())
    q=1
    for _ in range(q):
        n=int(input())
        l=list(map(int,input().split()))
        total=sum(l)
        if l[0]>(total//2):
            print(1)
            print(1)
        else:
            s=l[0]
            ans=[1]
            for i in range(1,n):
                if l[i]<=l[0]//2:
                    ans.append(i+1)
                    s+=l[i]
            if s>total//2:
                print(len(ans))
                print(*ans)
            else:
                print(0)
        