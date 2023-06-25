def program3236():
    from sys import maxsize
    
    n, l = map(int, input().split())
    cost = list(map(int, input().split()))
    min_rubles = 0
    prev = maxsize
    for i in range(31):
        if i < n:
            prev = min(2 * prev, cost[i])
        else:
            prev *= 2
        if l & (2 ** i):
            min_rubles += prev
        else:
            min_rubles = min(min_rubles, prev)
    
    print(min_rubles)