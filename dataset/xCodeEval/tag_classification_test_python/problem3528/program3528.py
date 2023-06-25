def program3528():
    k, a, b = map(int, input().split())
    
    if a < b:
    	a, b = b, a
    
    if a < k or (a%k != 0 and b < k):
    	print(-1)
    else:
    	print(a//k + b//k)