def program3076():
    # your code goes here
    n=input()
    A=sorted(map(int,input().split()))
    B=[]
    for x in A:
    	for i,y in enumerate(B):
    		if x>=y:
    			B[i]+=1
    			break
    	else:
    		B.append(1)
    print(len(B))
    		
    	