    #Problem 80B
    
def input():
    	st = input().split(":")
    	if(st[0][0] == "0"): st[0] = st[0][1:]
    	return (eval(st[0]), eval(st[1]))
    
def solve():
    	h, m = input()
    	h %= 12
    	h += float(m) / 60
    	return (h * 30, m * 6)
    
    
    res = solve()
    if(res[0] - int(res[0]) > 0): print '%0.1f %i' % res
    else: print '%0.0f %i' % res