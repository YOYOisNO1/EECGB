def program1796():
    import sys
    
    i = 0
    heights = ""
    for line in sys.stdin:
    	if i == 1:
    		heights = line.strip()
    	i+=1
    heights = heights.split(" ")
    for i in range(len(heights)):
        heights[i] = int(heights[i])
    heights.sort()
    ans = ""
    for i in range(len(heights)):
    	ans += str(heights[i]) + " "
    
    print(ans[:-1])