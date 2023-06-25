def program336():
    a,b=map(int,input().split())
    ct=0
    rem=240-b
    
    for x in range(1,a+1):
    	if rem - 5*x >=0:
    		ct+=1
    		rem-=5*x
    print(ct)