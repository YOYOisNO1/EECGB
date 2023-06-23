def program1246():
        # your code goes here
        a,b,c=map(int,input().split())
        if a==b:
        	print((c+a)*2)
        else:
        	x=min(a,b)
        	print((c+x)*2+1)