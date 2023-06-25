def program87():
    n, b, p = map(int, input().split())
    
    
    requiredItems = ''
    
    requiredB = (b*2) + 1
    waterBottles = 0
    
    while n > 1:
        waterBottles += (n/2) * requiredB
        n = (n/2) + (n%2)
    
    requiredItems += str(waterBottles)
    requiredItems += ' '
    requiredItems += str(n * p)
    
    print requiredItems