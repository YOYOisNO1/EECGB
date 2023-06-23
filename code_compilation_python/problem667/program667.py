def program667():
    # import sys
    # sys.stdin = open("test.in","r")
    # sys.stdout = open("test.out","w")
    n,k,t=map(int,input().split())
    if t<=k:
    	print(t)
    elif t<n and t>=k:
    	print(k)
    else:
    	print(n+k-t