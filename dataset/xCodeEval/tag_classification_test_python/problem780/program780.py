def program780():
    dic = {
    	'1': 2,
    	'2': 5, 
    	'3': 5,
    	'4': 4,
    	'5': 5,
    	'6': 6,
    	'7': 3,
    	'8': 7,
    	'9': 6,
    	'0': 6,
    }
    
    l, r = (map (int, input().strip().split()))
    ans = 0
    for i in range(l, r+1):
    	s = str(i)
    	for x in range(0, len(s)):
    		ans += dic[s[x]]
    print(ans)