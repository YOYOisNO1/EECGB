def program36():
    import sys
    
    a = sys.stdin.readline()
    
    if a == 1:
    	print(1)
    else:
    	print(9 * a * (a - 1) / 2 + 1 + 3 * (2 * a - 3))
    