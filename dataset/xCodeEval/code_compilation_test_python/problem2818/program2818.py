def program2818():
    l, r = list(map(int, input().split()))
    for i in range(l, r + 1):
    	a = [int(j) for j in str(i)]
    	if len(a) == len(set(a)):
    		print(i)
    		break
    	if i == r print(-1)