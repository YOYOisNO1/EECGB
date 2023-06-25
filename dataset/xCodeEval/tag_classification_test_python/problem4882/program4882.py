def program4882():
    n, k = map(int, input().split())
    
    l = [0]*n
    for i in range(k):
    	x = i % n
    	l[x] += 1
    print(len([i for i in l if i < 3]))