def program1279():
    n, k = [int(x) for x in input().split(' ')]
    candiesArja = 0
    candiesBran = 0
    candies = [int(x) for x in input().split(' ')]
    for i in range(n):
        candiesArja += candies[i]
        currCandies = candiesArja if candiesArja <=8 else 8
        candiesBran += currCandies
        candiesArja -= currCandies
        if candiesBran >= k:
            print(i+1)
            break
    else:
        print(-1)
    
    
    