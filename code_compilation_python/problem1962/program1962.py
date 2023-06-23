def program1962():
    n, k = map(int, input().split())
    candies = map(int, input().split())
    
    if sum(candies) < n or 8*n < k:
        print(-1)
        return
    
    arya=0
    maxc = 0
    day=0
    for candy_count in candies:
        arya += candy_count
        maxc += 8
        day+=1
        if arya >=k and maxc >= 8:
            print(day)
            break