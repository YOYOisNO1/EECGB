def program668():
    n = int(input())
    res = 0
    
    floors = 0
    maxCardForRooms = 0
    while maxCardForRooms < n:
        maxCardForRooms += 2+3*floors
        floors += 1
    if maxCardForRooms != n:
        floors -= 1
    for j in range(floors):
        if (n - 2*(j+1))%3 == 0:
            res += 1
    
    print(res)