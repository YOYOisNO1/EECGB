def program95():
    x,y = [int(no) for no in input().split()]
    n = int(input())
    f = [x,y]
    
    for i in range(n-2):
    	f.append((f[-1]-f[-2])%1000000007)
    
    if(n==1):
    	print(f[0]%1000000007)
    else:
    	print(f[-1]%1000000007)