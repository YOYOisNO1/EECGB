def program3425():
    k = input()
    q = input()
    ans = []
    cur = ""
    used = set()
    for i in range(len(q)):
    	if q[i] not in used:
    		if len(cur) > 0:
    			ans.append(cur)
     		cur = ""
    		cur += q[i]
    		used.add(q[i])
    	else:
    		cur += q[i]
    ans.append(cur)
    if len(ans) < k:
    	print("NO")
    else:
    	print("YES")
    	for i in range(k, len(ans)):
    		ans[k - 1] += ans[i]
    	for i in range(k):
    		print(ans[i])