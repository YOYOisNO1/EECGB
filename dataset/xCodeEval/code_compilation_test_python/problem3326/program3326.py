def program3326():
    # import sys 
    # sys.stdin=open("input1.in","r")
    # sys.stdout=open("OUTPUT3.out","w")
    for _ in range(int(input())):
    	N=int(input())
    	if N<=3:
    			print("1")
    	else:
    		S=3
    		arr=[]
    		arr.append(0)
    		arr.append(3)
    		for i in range(2,40):
    			S=S+pow(3,i)
    			arr.append(S)
    		for i in range(1,40):
    			if N>arr[i-1] and N<=arr[i]:
    				print(i)
    				break