def program192():
    n,d=map(int,input().split())
    n+=1
    count=0
    s='1'+input()
    pos=1
    while pos<n-1 and count<n:
        if s[pos]=='1':
            count+=1
            #print(f'pos: {pos} count: {count}' )
            pos+=d
        else:
            pos-=1
    if count>=n:
        print(-1)
    else:
        print(count)