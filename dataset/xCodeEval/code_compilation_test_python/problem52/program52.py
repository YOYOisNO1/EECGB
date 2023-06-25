def sum_digit(n):
        s=n%10
        while n//10:
            n=n//10
            s+=n%10
        return s
    n=int(input())
    m=0
    for i in range(1,n//2+1):
        a=sum_digit(i)
        b=sum_digit(n-i)
        m=max(m,a+b)
    print(m)