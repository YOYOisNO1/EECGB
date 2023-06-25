def all_substrings(s):
    	l = set([])
    	for i in range(0, len(s)):
    		for j in range(1, len(s)+1):
    			l.add(s[i:j])
    #	print(l)
    	m = -1
    	for substring in l:
    		c = occurrences(s, substring)
    		if c> 1:
    			m = max(m, len(substring))
    	if m == -1: return 0
    	return m
    
def occurrences(string, sub):
        count = start = 0
        while True:
            start = string.find(sub, start) + 1
            if start > 0:
                count+=1
            else:
                return count
    
    r = input().strip()
    print(all_substrings(r))
    #print(all_substrings('abcd'))
    #print(all_substrings('ababa'))
    #print(all_substrings('zzz'))		