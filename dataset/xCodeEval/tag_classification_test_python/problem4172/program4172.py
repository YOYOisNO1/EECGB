def program4172():
    import math
    
    houses, goal = map(int, input().split())
    if(goal%2 == 0):
        print((houses-goal)//2+1)
    else:
        print(math.ceil(goal/2))