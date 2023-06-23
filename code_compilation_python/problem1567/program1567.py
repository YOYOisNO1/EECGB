def program1567():
    if __name__ =="__main__":	
    	n = int(input())
    	arr = list(map(int,input().split()))
    	if max(arr)<=25:
    		print(0)
    	else:
    	    x = n
    		if 1 not in arr:
    			arr.append(0)
    			x+=1
    		ans = 0
    		arr.sort()
    		for i in range(1,x):
    			ans += (arr[i]-arr[i-1]-1)
    		print(ans-(25-n))