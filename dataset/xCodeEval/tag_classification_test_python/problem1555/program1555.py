def program1555():
    n=int(input())
    s1=str(input())
    
    for i in range(1,n//2+1):
    	if(n%i==0):
    		s2=s1[0:i]
    		s3=s1[i:len(s1)]
    		s1=s2[::-1]+s3
    print(s1[::-1])