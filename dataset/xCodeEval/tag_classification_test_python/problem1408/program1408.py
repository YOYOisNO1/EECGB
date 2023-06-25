def program1408():
    k,n,w=[int(x) for x in input().split()]
    s=((k+(k*w))*(w/2))
    if n>s:
    	print(0)
    else:
    	print(int(s-n))