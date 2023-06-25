def program1334():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum = [0,0,0,0,0]
    countA = [0,0,0,0,0]
    countB = [0,0,0,0,0]
    flag = 0
    
    for x in range(0,n):
    	for i in range(0,5):
    		if a[x] == i+1:
    			sum[i] += 1
    			countA[i] += 1
    		if b[x] == i+1:
    			sum[i] += 1
    			countB[i] += 1
    #print(sum)
    #print(countA)
    #print(countB)
    
    ans = 0
    
    for i in range(0,5):
    	#s = "ans = " + str(ans) + ", sum[i] = " + str(sum[i]) + ", sum[i]/2 = " + str(sum[i]/2) + ", countA[i] = " + str(countA[i])
    	#print(s)
    	ans += abs(sum[i]/2 - countA[i])
    
    if ans % 2 == 1:
    	print("-1")
    else:
    	print(int(ans/2))
    
    
    