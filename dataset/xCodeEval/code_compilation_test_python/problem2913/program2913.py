def deco(num):
    	arr = []
    	count = 9
    	if num < 10:
    		return num
    	while num >= 10 or num in arr:
    		num = num - count
    		arr.append(count)
    		count = count - 1
    	if num > 0:
    		arr.append(num)
    
    	arr.sort()
    	#print(arr)
    	return int(''.join(map(str,arr)))
    
    
    
    n = int(input())
    while (n=!0):
    	s = int(input())
    	deco(s)
    	n -=1