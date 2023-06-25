def program1459():
    f1 = list(map(int,input().split()))
    f2 = list(map(int,input().split()))
    
    f=0
    for i in range(3):
    	if f1[i]==f2[i]:
    		f=1
    		break
    
    if f==0:
    	print("NO")
    else:
    	print("YES")