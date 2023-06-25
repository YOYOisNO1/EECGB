def program3890():
    n = int(input())
    arr = sorted(map(int, input().split()), reverse=True)
    used = set()
    out = 0
    for i in arr:
    	while i in used:
    		i -= 1
    	if i > 0:
    		out += i
    		used.add(i)
    
    print(out)