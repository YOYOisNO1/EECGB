def program2262():
    a,b=map(int,input().split())
    t=list(map(int,input().split()))
    t=sorted(t)
    t=t[::-1]
    c=t[b-1]
    cnt=0
    for i in t:
            if i>=c and i>0:
                    cnt+=1
    print(cnt)