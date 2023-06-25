def program1657():
    n = int(input())
    a = map(int, input().split())
    first = a.pop(0)
    a.sort()
    after = first
    i = n-2
    while after <= max(a):
    	after += 1
    	a[-1] -= 1
    	a.sort()
    	#print(a)
    
    print(after) - first