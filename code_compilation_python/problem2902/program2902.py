def program2902():
    n = int(input())
    cubesused = 0
    cubesleft = n
    floors = 1
    
    if  n <= 3:
        print(1)
    elif n > 3 and <= 9:
        print(2)
    else:
        for i in range(n):
            if (((floors) * (floors+1)) / 2) <= cubesleft:
                floors +=1
                cubesleft -= (((floors) * (floors+1)) / 2)
            else:
                print(floors)
                break
                