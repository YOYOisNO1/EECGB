def program1323():
    import math
    n, k = list(map(int, input().split()))
    t = 1
    for i in range(k):
    	t *= 10
    print(n * t // math.gcd(n, t))