def program1477():
    n = {
    	0 : 6,
    	1 : 8,
    	2 : 4,
    	3 : 2,
    }
    i = int(input())
    if i != 0: print(n[i % 4])
    else: print(1)