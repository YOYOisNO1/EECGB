def program2985():
    n=int(input())
    a=sorted(list(map(int,input().split())))
    cnt1=0
    cnt2=0
    d=n
    for i in range(1,n//2+1):
        #print(d-a[-i])
        cnt1+=abs(d-a[-i])
        cnt2+=abs(d-1-a[-i])
        d-=2
    print(min(cnt1,cnt2))
    
    
    