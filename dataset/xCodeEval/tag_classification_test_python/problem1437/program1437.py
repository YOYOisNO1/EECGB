def program1437():
    #!/usr/bin/env python3
    
    if __name__ == "__main__":
    	n, m = map(int, input().split())
    	a = list(map(int, input().split()))
    	b = list(zip(range(1, n+1), a))
    	c = 1
    	while len(b) != 1:
    		flag = 0
    		dlt = []
    		for i in range(len(b)):
    			if b[i][1] > c*m:
    				b.append(b[i])
    				flag = 1
    				dlt.append(i)
    		for i in range(len(dlt)):
    			del b[dlt[i] - i]
    		c += 1
    		if flag == 0:
    			break
    	print(b[-1][0])