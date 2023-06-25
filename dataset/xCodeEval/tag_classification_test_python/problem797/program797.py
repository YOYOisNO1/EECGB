def program797():
    g, a = [], [int(i) for i in input().split()]
    for i in range(2,61):
        g += [int(2**i-1)^(2**j) for j in range(i-1)] 
    print(sum([1 for i in sorted(g) if a[0] <= i <= a[1]]))