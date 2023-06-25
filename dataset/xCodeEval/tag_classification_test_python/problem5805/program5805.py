def program5805():
    import sys,math
    from fractions import gcd
    from bisect import bisect_left, bisect
    from collections import defaultdict
    from io import BytesIO
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda: sys.stdin.readline().rstrip('\r\n')
    n = int(input())
    arr = [int(_) for _ in input().split()]
    a = 'Alice'
    b = 'Bob'
    
    m = min(arr)
    num = arr.count(m)
    
    print(a if num <= n//2 else b)