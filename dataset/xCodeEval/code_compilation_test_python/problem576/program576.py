def program576():
    n=int(input())
    s=input()
    f=[0 for i in range(0,n)]
    f[0]=1
    for i in range(1,n):
    	f[i]=f[i-1]+1
    	for j in range(0,i):
    		if s[2*j-i-1:j]==s[j:i+1]:f[i]=min(f[i],f[j-1]+1)
    print(f[-1])