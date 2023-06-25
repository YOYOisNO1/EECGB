def program1885():
    #Even Odds
    from math import ceil
    
    s = input()
    arr = map(int, s.split(" "))
    n = arr[0]
    k = arr[1]
    
    if k <= ceil((n+0.0)/2):
    	print(2*k) - 1
    else:
    	print(int(2*(k) - ceil(((n+0.0)/2))))