def gcd(a, b):
        while (b != 0):
            a, b = b, a % b
        return a
    
    n = int(input())
    crush = list(map(int, input().split()))
    ans = 1
    
    for i in range(n):
        j = crush[i] -1
        c = 1
        while (i != j and c < n + 1):
            c += 1
            j = crush[j] - 1
        if c > n:
            ans = -1
            break
        if c % 2 == 0:
            c //= 2
        ans = ans * c // gcd(ans, c)
            
    
    print(ans)