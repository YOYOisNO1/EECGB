def program3250():
    from collections import defaultdict
    
    
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    
    costs = defaultdict(lambda: [])
    
    for ai in a:
        cost = 0
        costs[ai].append(cost)
        while ai != 0:
            ai //= 2
            cost += 1
            costs[ai].append(cost)
    
    min_cost = 99999999
    for key, item in costs.items():
        if len(item) >= k:
            k_cost = sum(sorted(item[:k]))
            if k_cost < min_cost:
                min_cost = k_cost
    
    print(min_cost)