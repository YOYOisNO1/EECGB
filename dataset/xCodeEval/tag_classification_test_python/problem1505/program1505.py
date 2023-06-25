def program1505():
    a,b=map(int,input().split())
    r=a+1
    l=-1
    while(r-l>1):
            m=(l+r)//2
            if((a-m)*(a-m+1)//2-m>b):
                    l=m
            else:
                    r=m
    print(r)