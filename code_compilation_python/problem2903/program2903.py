def program2903():
    n = int(input())
    cubesused = 0
    cubesleft = n
    floors = 1
    
    if  n =< 2:
        print(1)
    else:
        for i in range(n):
            if (((floors) * (floors+1)) / 2) <= cubesleft:
                floors +=1
                cubesleft -= (((floors) * (floors+1)) / 2)
            else:
                print(floors)
                break
                