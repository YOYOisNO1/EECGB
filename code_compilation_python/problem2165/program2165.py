def program2165():
    x=0
    z=[]
    y=int(input())
    count=0
    for i in range (y):
    	z.append(input())
    for i in z:
        if i== "++X" or i =="X++":
            count+=1
        else:
            count-=1
     print(count)