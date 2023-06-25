def program7771():
    from sys import stdin
    
    sum_n = lambda n: n > 0 and (n * (n + 1)) // 2
    sum_odd = lambda n: n > 0 and n * n
    
    n, x, y, c = [int(x) for x in stdin.readline().split()]
    ans, cur = 0, 1
    
    while cur < c:
        ans += 1
        up, down, left, right = 1 - x + ans, x + ans - n, 1 - y + ans, y + ans - n
    
        cur = sum_n(ans) * 4 + 1 - sum_odd(up) - sum_odd(down) - sum_odd(left) - sum_odd(right)
        cur += sum_n(right - x) + sum_n(right - n + x - 1) + sum_n(left - x) + sum_n(left - n + x - 1)
    
    print(ans)