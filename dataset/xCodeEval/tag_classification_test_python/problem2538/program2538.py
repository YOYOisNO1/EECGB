def program2538():
    x,y=input().split(" ")
    x=int(x)
    y=int(y)
    list1 = [int(i) for i in input().split()]
    list1.sort()
    min=list1[y-1]
    for i in range(0,y-x+1):
    	if(list1[i+x-1]-list1[i]<min):
    		min=list1[i+x-1]-list1[i]
    if(y-x==0):
    	print(list1[y-1]-list1[0])
    else:
    	print(min)