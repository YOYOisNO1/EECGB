def program3992():
    w, m = map(int, input().split())
    for i in range(100, -1, -1):
    	if abs(w**i - m) < m:
    		m = abs(w**i - m)
    if m == 0:
    	print("YES")
    else:
    	print("NO")