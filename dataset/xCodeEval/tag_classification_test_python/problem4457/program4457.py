def program4457():
    from math import log
    
    x, y = map(int, input().split())
    p = y*log(x) - x*log(y)
    if (p > 0):
    	print(">")
    elif (p < 0):
    	print("<")
    else:
    	print("=")