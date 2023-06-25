def gcd(aa, b):
        while b != 0:
            aa, b = b, aa % b
        return aa
    
    n = int(input())
    a = [i - 1 for i in list(map(int, input().split()))]
    ans = 1
    for i in range(n):
        j = a[i]
        c = 1
        while i != j and c <= n:
            c += 1
            j = a[j]
        if c > n:
            ans = -1
            break
        if c % 2 == 0:
            c //= 2
        ans = ans * c // gcd(ans, c)
    print(ans)