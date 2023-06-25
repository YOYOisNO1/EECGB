def program2692():
    import math
    
    n, k = [int(x) for x in input().split(' ')]
    ans = 0
    ans += int(math.ceil(2.0 * n / k))
    ans += int(math.ceil(5.0 * n / k))
    ans += int(math.ceil(8.0 * n / k))
    print(ans)