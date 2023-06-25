    '''
    t가 계속 s에 속하게 하면서(개수와 순서만 맞으면됨)
    최대의 연속된 문자를 제거하는 방법은?
    
    --> 그냥 모든 문자를 제거해가면서 최고의 경우의수를 찾아내자
    '''
    
    s = input()
    t = input()
    
def check(s):
    	ans = 0
    	for i in s:
    		if ans == len(t):
    			break
    		if i == t[ans]:
    			ans += 1
    	return ans == len(t)
    ans = 0
    
    ## check every case of deleting substring
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if check(s[:i] + s[j:]):
                ans = max(j - i, ans)
    print(ans)