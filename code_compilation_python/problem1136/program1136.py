def program1136():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.append(-100000000000)
    arr.append(1000000000000)
    i = 0
    while(arr[i] < arr[i+1] && i < n-1):
    	i = i + 1
    
    while(arr[i] == arr[i+1] && i < n-1):
    	i = i + 1
    
    while(arr[i] > arr[i+1] && i < n-1):
    	i = i + 1
    
    if(i == n-1):
    	print("YES")
    
    else:
    	print("NO")
    
    
    