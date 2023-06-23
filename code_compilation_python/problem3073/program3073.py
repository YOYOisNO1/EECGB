    """
    给你一个字符串s，你可以将每个字符任意涂红色或者黑色。然后对于任何相邻两个不同颜色的字符，你都可以将它们交换。问是否存在一种涂色方案，在经过有限次swap后使得整个字符串是升序排列。
    """
def colorable(s):
    	mn = ""
    	n = len(s)
    	res = "0"
    
    	for i in range(1, n):
    		if s[i] < s[i-1]:
    			if s[i] < mn:
    				return False, res
    			mn = s[i]
    			res += "1"
    		else:
    			res += "0"
    	return True, res
    
    n = input()
    s = input()
    
    valid, res = colorable(s)
    if valid:
    	print("YES")
    	print(res)
    else:
    	print("NO")