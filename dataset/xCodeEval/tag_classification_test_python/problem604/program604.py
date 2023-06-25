def program604():
    n=int(input())
    s=0
    for j in range(1,n):
    	s=s+j*(n-j)
    print(s+n)