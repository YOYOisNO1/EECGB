def program895():
    import math
    
    houses = int(input())
    goal = int(input())
    if(goal%2 == 0):
        print((houses-goal)//2+1)
    else:
        print(math.ceil(goal/2))