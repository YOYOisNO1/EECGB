    n, k = map(int, input().split())
    
    
def euler(n):
        res = n
        i = 2
        while i * i <= n:
            if n % i == 0:
                res = res / i * (i - 1)
                while n % i == 0:
                    n /= i
            i += 1
        if n != 1:
            res = res / n * (n - 1)
        return res
    
    
    while k > 0 and n > 1:
        if(k%2==1):
            n = euler(n)
        k-=1
    print  n%1000000007