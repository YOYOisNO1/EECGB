def program7518():
    left, right = 0, 0
    maxstuds = 0
    n = input()
    l = map(int, input().split())
    l.sort()
    t = input()
    while right < n:
    	if l[right] - l[left] > t:
    		left += 1
    	else:
    		maxstuds = max(maxstuds, right - left + 1)
    		right += 1
    if l[-1] - l[left] <= t:
    	maxstuds = max(maxstuds, n - left)
    print(maxstuds)