    n,m,k=map(int,input().split())
    if (k==-1) and (n&1)^(m&1):
        print("0");
    else :
    def pow1(a,b,n):
            result=0;
            x=a;
            while(b):
                if(b&1):
                    result=((result)*a%n)
                x=x*x%n;
                b=b<<1
            return result
        a=pow(2,(n-1)*(m-1),1000000007);
        print(a)