def program4325():
    a=[]
    i=1
    while i<=1000:
    	a.append(str(i))
    	i=i+1
    a=''.join(a)
    n=int(input())
    print(a[n-1])
    