def program7034():
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    ans = 0
    w = 1
    while n > 1:
        cnt = n // 2
        ans += w * cnt
        n = (n + 1) // 2
        w <<= 1
    print(ans)