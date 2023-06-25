def program2313():
    n = int(input())
    count = 0
    while n >= 100000:
        n = n - 100000
        count += 1000
    
    while n >= 100:
        n = n - 100
        count += 1
    
    while n >= 20:
        n = n - 20
        count += 1
    
    while n >= 10:
        n = n - 10
        count += 1
    
    while n >= 5:
        n = n - 5
        count += 1
    while n >= 1:
        n = n - 1
        count += 1
    print(count)