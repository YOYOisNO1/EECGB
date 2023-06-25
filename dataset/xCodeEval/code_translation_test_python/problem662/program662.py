def program662():
    n,v = list(map(int,input().split()))
    
    if (n-1)<v:
    	ans = n-1
    else:
    	ans = v + (n-v)*(n-v+1)/2 - 1
    
    print(int(ans))