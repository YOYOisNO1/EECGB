def program1275():
        n,m=map(int,input().split())
        p = 1000000007
        x=(int)(pow(2,m,p))-1;
        y=(int)(pow(x,n,p));
        print(y);