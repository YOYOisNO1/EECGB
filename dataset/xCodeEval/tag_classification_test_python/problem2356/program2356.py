def f(n):
        i = 2
        while i*i<=n:
            if n%i==0:
                return i
            i+=1
        return n
    n = int(input())
    ans = 0
    if n%2==0:
        print(n//2)
    else:
        a = f(n)
        n-=a
        print((n//2)+1)