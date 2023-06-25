    c=int(input())
    m=int(input())
    n=int(input())
def gcd(n,m):
        if m==0:
            return n
        else:
            return gcd(m,n%m)
    if c%gcd(n,m)==0:
        f=0
        x=c//n
        while x>=0:
            if (c-x*n)%m==0:
                f=1
                break
            else:
                x-=1
        if f==1:
            y=(c-x*n)//m
            print('YES')
            print(y,x)
        else:
            print('NO')    
            
    else:
        print('NO')      