def program2587():
    n,m=map(int,input().split())
    d=n
    count=0
    while(m>n):
        if(m%2==0):
            m=m//2
            count+=1
        else:
            count+=1
            m+=1
    print(abs(count+n-m))
            