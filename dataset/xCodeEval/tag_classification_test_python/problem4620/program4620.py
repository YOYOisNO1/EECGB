def program4620():
    n,k = map(int, input().split())
    s = str(input())
    f = [[0]*26for j in range(2)]
    for i in range(26):
    	aa = s.find(chr(65+i))
    	bb = s.rfind(chr(65+i))
    	f[0][i] = aa
    	f[1][i] = bb
    lmin = max(f[0])
    ans = 0
    for i in range(26):
    	if f[1][i] >= lmin:
    		ans += 1
    if ans <= k:
    	print('NO')
    else:
    	print('YES')