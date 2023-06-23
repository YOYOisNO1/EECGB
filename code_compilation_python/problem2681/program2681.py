def program2681():
    pikachu = [int(x) for x in input().split(' ')]
    N = pikachu[0]
    C = pikachu[1]
    
    maxdrop = 0
    prices = [int(x) for x in input().split(' ')]
    for i in range(len(prices) - 1):
        diff = prices[i] - prices[i+1]
        if (diff > maxdrop):
            maxdrop = diff
    
    print (maxdrop - C)