    # f = open('test.py')
# def input():
    # 	return f.readline().replace('\n','')
    
    # import heapq
    # import bisect
    # from collections import deque
    # from collections import defaultdict
def read_list():
    	return list(map(int,input().split(' ')))
def print_list(l):
    	print(' '.join(map(str,l)))
    
    output = [1] * 35000
def countPrimes(n):
        output[0],output[1] = 0,0
        for i in range(2,int(n**0.5)+1): 
            if output[i] == 1:
                output[i*i:n:i] = [0] * len(output[i*i:n:i])
    countPrimes(35000)
    s = [i for i in range(35000) if output[i]==1]
    
    N = int(input())
    for _ in range(N):
    	n = int(input())
    	flag = True
    	for k in s:
    		if n%k==0:
    			tmp = n//k
    			print('%d %d'%(tmp,n-tmp))
    			flag = False
    			break
    	if flag:
    		print('%d %d'%(1, n-1))