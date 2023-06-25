def program2316():
    n, m = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    b = list(map(int, input().split(' ')))
    
    x = min(a)
    y = min(b)
    ans = set()
    
    if x == y:
    	ans.add(x)
    else:
    	ans.add(min(x, y) * 10 + max(x, y))
    	for i in a:
    		if i in b:
    			ans.add(i)
    		
    print(min(ans))