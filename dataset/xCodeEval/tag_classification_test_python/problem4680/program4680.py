def program4680():
    n, ka = [int(x) for x in input().split()]
    # print(k+"ll")
    gates = input()
    open1 = dict()
    close = dict()
    count = 0
    for k in gates:
    	if k not in open1:
    		open1[k] = count
    	close[k] = count
    	count += 1
    arr = [0 for x in xrange(1000006)]
    for key in open1:
    	arr[open1[key]] += 1
    for key in close:
    	arr[close[key]+1] -= 1
    # print(arr[0:n+1])
    count = 0
    for i in arr[0:n+1]:
    	count += i
    	# print(count) - ka
    	if(count > ka):
    		print("YES")
    		exit()
    print("NO")