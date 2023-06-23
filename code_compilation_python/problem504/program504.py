def program504():
    x,y,z= [input() for _ in range(3)]
    newword = x+y
    count =0
    for i in newword:
    	if newword.count(i)==z.count(i):
    		count+=1
    print("YES") if count==len(z) else print("NO")