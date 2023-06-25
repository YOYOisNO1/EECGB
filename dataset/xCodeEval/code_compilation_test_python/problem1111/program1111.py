def program1111():
    x=int(input())
    if x==1:
    	print(-1)
    	break
    for i in range(2,101):
    	if x%i==0:
    		p=i
    		break
    print(x,i)