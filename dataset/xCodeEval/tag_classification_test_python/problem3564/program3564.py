def program3564():
    N, T = map(int, input().split())
    S = input()
    slist = []
    for i in range(0, N):
    	slist.append(S[i])
    for i in range(0, T):
    	changelist = []
    	for j in range(0, N-1):
    		if slist[j] == 'B' and slist[j+1] == 'G': changelist.append(j)
    	for k in range(0, len(changelist)):
    		tmp = slist[changelist[k]]
    		slist[changelist[k]] = slist[changelist[k]+1]
    		slist[changelist[k]+1] = tmp
    ans = ''
    for i in range(0, N):
    	ans = ans + slist[i]
    print(ans)