def program944():
    x = int(input())
    y = input()
    k=0
    j=0
    for i in range(x):
    	if y[i]=='S'&&y[i+1]=='F':
    		k=k+1
    	else:
    		j=j+1
    if(k>j):
    	print("Yes")
    else:
    	print("No")	