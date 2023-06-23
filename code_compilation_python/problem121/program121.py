def program121():
    n = int(f.readline())
    
    arr = sum([int(x) for x in input().split()])
    
    for x in range(1,6):
        if (arr +x)%(n+1) == 0:
            print(x)
            break