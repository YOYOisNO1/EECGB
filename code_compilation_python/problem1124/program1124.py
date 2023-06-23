def program1124():
    n, k = map(int, input().split())
    a = []
    for x in range(1, int(n**0.5)+1):
    	if n % x == 0:
    		a.append(x)
    		if x**2 != n:
    			a.append(n//x)
    print(sorted(a)[k-1] if k <= len(a) else -1)
    →Протокол тестирования