    input = input
    
def sol1():
    	n = int(input())
    	arr = [int(i) for i in input().split()]
    	min_val = min(arr)
    	mins = [i for i in range(n) if arr[i]==min_val]
    	diff = [mins[i+1]-mins[i] for i in range(len(mins)-1)]
    	print(min(diff))
    
def sol2():
    	n,a,b = [int(i) for i in input().split()]
    	'''
    	totMin = 0
    	for i in range(1,n):
    		curMin = min(a//i, b//(n-i))
    		totMin = max(totMin,curMin)
    	print(totMin)
    	'''
    	print(max([min(a//i, b//(n-i)) for i in range(1,n)]))
    
    if __name__=='__main__':
    	sol2()