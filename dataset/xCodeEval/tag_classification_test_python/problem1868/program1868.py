def program1868():
    A=input()
    if(A[-1]!=('a') and A[-1]!='e' and A[-1]!='i' and A[-1]!='o' and A[-1]!='u' and A[-1]!='n'):
    	print("NO")
    	exit()
    for i in range(0,len(A)-1):
    	if(A[i]!=('a') and A[i]!='e' and A[i]!='i' and A[i]!='o' and A[i]!='u' and A[i]!='n' ) and A[i+1]!=('a') and A[i+1]!='e' and A[i+1]!='i' and A[i+1]!='o' and A[i+1]!='u'  :
    		# print(A[i],A[i+1])
    		print("NO")
    		exit()
    print("YES")