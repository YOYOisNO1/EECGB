def Diary():
    	n = int(input())
    	arr = []
    	for i in range(n):
    		arr.append(list(map(int, input().split())))
    	s = 0
    	midNum = n//2
    	midNumber = arr[midNum][midNum]
    	s += sum(arr[n//2])
    	for i in range(n):
    		s += arr[i][midNum]
    		s += arr[i][i]
    		s += arr[n-1-i][i]
    	s -= 3 * midNumber
    	print(s)
    
    
    
    
    Diary()