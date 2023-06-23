def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    n=int(input());a=int(input());b=int(input())
    i=0
    if n%(gcd(a,b))!=0:
        print('NO')
    else:
        while i*a<=n:
            if (n-(i*a))%b==0:
                print('YES')
                print(i,(n-(i*a))//b)
                exit(0)
            else:i+=1
        print('NO'