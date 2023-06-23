def program1359():
    n = int(input())
    res = 0
    
    if n < 5:
        res = 1
    else:
        floor = 1
        maxCardForRooms = 2
        while maxCardForRooms < n:
            if (n - 2*floor)%3 == 0:
                res += 1
            floor += 1
            maxCardForRooms = 0
            for i in range(floor):
                maxCardForRooms += 2+3*i
        if maxCardForRooms == n :
            res += 1
    
    print(res)