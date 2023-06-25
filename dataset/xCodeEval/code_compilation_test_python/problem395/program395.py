def program395():
    a1=input().split()
    a=int(a1[0])
    b=int(a1[1])
    n=0
    for i in range(a,b+1):
    	if bin(i).count('0')==2:
    		n+=1
    print(n)