def program3884():
    for _ in range(int(input())):
        n = int(input())
        if (n%2==0):
            print(n//2,n//2)
        else:
            m=(int(n**(1/2))+1)
            x=1
            while (m>1):
                if (n%m==0):
                    x=max(m,n//m)
                m-=1
            print(x,n-x)