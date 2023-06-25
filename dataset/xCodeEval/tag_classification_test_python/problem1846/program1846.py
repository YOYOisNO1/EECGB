def program1846():
    n, m = map(int,input().split())
    m = m/n
    
    if m%1!=0:
        print(-1)
    else:
        cnt=0
        while m%6==0:
            cnt+=2
            m=m/6
        while m%2==0:
            cnt+=1
            m=m/2
        while m%3==0:
            cnt+=1
            m=m/3
        if m==1:
            print(cnt)
        else:
            print(-1)