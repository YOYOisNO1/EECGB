def program3650():
    import sys
    
    buyers, cost_per_apple = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
    buyer_descriptions = [i.rstrip() for i in sys.stdin.readlines()]
    
    total_cost = counter = 0
    
    for buyer in buyer_descriptions:
        if buyer == 'halfplus':
            counter += 1
            total_cost += counter*cost_per_apple
            counter *= 2
        elif buyer == 'half':
            total_cost += counter*cost_per_apple
            counter *= 2
    
    print total_cost / 2