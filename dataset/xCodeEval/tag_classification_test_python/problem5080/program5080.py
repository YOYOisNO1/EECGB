def program5080():
    n,a,b,c,d = map(int,input().split())
    s1,s2,s3,s4 = a+b,a+c,b+d,c+d
    minSum = max(s1,s2,s3,s4)+1
    maxSum = min(s1,s2,s3,s4)+n
    print(max(maxSum-minSum+1,0)*n)