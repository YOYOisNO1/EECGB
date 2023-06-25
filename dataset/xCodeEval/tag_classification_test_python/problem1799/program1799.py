    a,b=[int(x) for x in input().split()]
    lcm=K=10**100
def gcd(a,b):
        if b>a:
            a,b=b,a
        if b==0:
            return a
        return gcd(a%b,b)
    delit=[]
    if a==b:
        print(0)
    else:
        if a>b:
            a,b=b,a
        for i in range(1,int((b-a)**0.5)+1):
            if (b-a)%i==0:
                delit.append(i)
                delit.append((b-a)//i)
        for item in delit:
            if a%item==0:
                k=0
            else:
                k=item-(a%item)
            if (a+k)*(b+k)//(gcd(b-a,a+k))<lcm:
                lcm=(a+k)*(b+k)//(gcd(b-a,a+k))
                K=k
            elif (a+k)*(b+k)//(gcd(b-a,a+k))==lcm and k<K:
                K=k
        print(K)
            