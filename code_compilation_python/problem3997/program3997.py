def program3997():
    (n, m, min, max) = map(int, input().split())
    
    temps = [int(input()) for i in range(0,m)]
    
    if(n - m >= 2 or n - m is 0):
        print("Correct")
    else:
        hasMin = False
        hasMax = False
        temps.sort()
        if(temps[0] <= min):
            hasMin = True
        if(temps[m - 1] >= max):
            hasMax = True
        
        if(hasMin and hasMax):
            print("Correct")
        elif((hasMin or hasMax) and n-m is 1):
            print("Correct")
        else:
            print("Incorrect")