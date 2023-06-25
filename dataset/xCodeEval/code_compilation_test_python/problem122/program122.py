def program122():
    n = int(input())
    
    fingers = 0
    for _ in range(n):
    	fingers = sum([int(x) for x in input().split()])
    
    ways = 0
    for i in range(1,6):
    	if (i+fingers) % (n+1) != 1:
    		ways += 1
    
    print(ways)