def program1317():
    d1=(input(""))
    d2=(input(""))
    d3=(input(""))
    
    L1=d1.split()
    L2=d2.split()
    L3=d3.split()
    for i in range(len(L1)):
    	L1[i]=int(i)
    for i in range(len(L2)):
    	L2[i]=int(i)
    	for i in range(len(L3)):
    	L3[i]=int(i)
    n=L1[2]	
    print(L1)
    if min(L2)>=max(L3):
    		print(int(n))
    
    else:
    		a=(int(n)//int(min(L2)))*int(max(L3))+int(n)%int(min(L2))
    		print(int(a))
    	