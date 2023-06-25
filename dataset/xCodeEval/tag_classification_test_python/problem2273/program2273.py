def program2273():
    a = []
    for _ in range(4):
        a.append(int(input()))
    
    d = int(input())
    
    da = [False] * (d + 1)
    
    count = 0
    for x in a:
        for val in range(x, d + 1, x):
            if not da[val]:
                count += 1
                da[val] = True
            
    print(count)
                