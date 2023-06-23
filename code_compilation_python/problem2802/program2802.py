def program2802():
    n, m, k = map(int, input().split())
    costs = [int(x) for x in input().split()]
    
    for i in range (1, n):
        if m+i < n and costs[m+i] <= k:
            print(i)
            exit(0)
        elif m-i >= 0 an dcosts[m-i] <= k:
            print(i)
            exit(0)
            