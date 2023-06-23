def program156():
    arr = input()
    
    count = 1
    while count != 7:
    	for i in range(len(arr) - 1):
    		if arr[i] == arr[i + 1]:
    			count += 1
    		else:
    			count = 0
    		
    
    if count >= 7:
    	print("YES")
    else:
    	print("NO")