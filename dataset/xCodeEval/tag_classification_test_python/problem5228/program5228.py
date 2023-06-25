def program5228():
    a=input()
    x,y=list(map(str,input().split()))
    p=[ "6", "7", "8", "9", "T", "J", "Q", "K" , "A"]
    if(x[1]==a and y[1]!=a):
    	print("YES")
    elif((x[1]==a and y[1]==a) or x[1]==y[1]):
    	if(p.index(x[0])>p.index(y[0])):
    		print("YES")
    	else:
    		print("NO")
    else:
    	print("NO")