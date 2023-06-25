def program1170():
    T=input()
    S=input().split()
    A=S[0]
    B=S[1]
    L={'6':0,'7':1,'8':2,'9':3,'T':4,'J':5,'Q':6,'K':7,'A':8}
    flag1=False
    flag2=False
    if(A[1]==T):
    	flag1=True
    if(B[1]==T):
    	flag2=True
    if(flag1 and flag2):
    	if(L[A[0]]>L[B[0]]):
    		print("YES")
    	else:
    		print("NO")
    elif(flag1):
    	print("YES")
    elif(flag2):
    	print("NO")
    else:
    	if(A[1]==B[1] and L[A[0]]>L[B[0]]):
    		print("YES")
    	else:
    		print("NO")