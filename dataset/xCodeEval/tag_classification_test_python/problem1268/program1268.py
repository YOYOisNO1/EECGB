def program1268():
    n,m,r=map(int,input().split());o=0
    while(m<n):
            m*=r;o+=1
    print(o)