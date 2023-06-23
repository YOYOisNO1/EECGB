def program408():
    n,s=map(int,input().split())
    l=list(map(int,input().split()))
    a=int(0)
    for i in range(n):
        a+=l[i]
    if s < (a + (n - 1) * 10)):
    		print(-1)
    else :
    		print(s - a) / 5)
    	