    from math import ceil
    
def odd(r, l):
    	return int(ceil(r/2.0) - ceil((l-1.0)/2.0))
    
def even(r, l):
    	return r/2 - (l-1)/2
    
    x1, y1, x2, y2 = map(int, input().split())
    NORM = int(1e9 + 2)
    print(odd(y2-y1+NORM,) NORM)*odd(x2-x1+NORM, NORM) + even(y2-y1+NORM, NORM)*even(x2-x1+NORM, NORM)