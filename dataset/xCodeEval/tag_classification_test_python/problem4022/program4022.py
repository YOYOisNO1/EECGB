def program4022():
    from collections import Counter
    w,m=map(int, input().split())
    d=Counter()
    cnt=0
    while m:
        d[cnt]=m%w
        m/=w
        cnt+=1
    for i in range(cnt+1):
        if d[i] not in [0,1,w-1,w]:
            print('NO')
            exit()
        else:
            if d[i]==w-1 or d[i]==w:
                d[i+1]+=1
    print('YES')