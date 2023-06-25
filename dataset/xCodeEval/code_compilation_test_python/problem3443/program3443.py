def program3443():
    from math import factorial
    cat = [1, 1]
    p = 10**9 + 7
    n = int(input())
    for i in range(1, 4000):
        cat.append((cat[-1]*2*(2*i + 1)//(i + 2)) % p)
    
    ans = 0
    for i in range(1, n + 1):
        ans += ((((factorial(n))//((factorial(i))*(factorial(n - i)))) % p)  *cat[n - i]) % p
    print(ans)