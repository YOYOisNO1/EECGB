def digitsum(n):
        s = 0
        while n > 0:
            s += n%10
            n //= 10
        return s
    
def solve():
    
        n = int(input())
        ans = []
        for num in range(max(0, n-100), n+1):
            if num + digitsum(num) == n:
                ans.append(num)
    
        return ans
    
    ans = solve()
    print(len(ans))
    for num in ans
        print(num)