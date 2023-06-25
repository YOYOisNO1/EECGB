def program1106():
    a1,a2,a3=map(int,input().split())
    b1,b2,b3=map(int,input().split())
    c1,c2,c3=map(int,input().split())
    r1=[True,True,True]
    r2=[True,True,True]
    r3=[True,True,True]
    if(a1%2!=0):
    	r1[0]=not r1[0]
    	r1[1]=not r1[1]
    	r2[0]=not r2[0]
    if(a2%2!=0):
    	r1[1]=not r1[1]
    	r1[0]=not r1[0]
    	r1[2]=not r1[2]
    	r2[1]=not r2[1]
    if(a3%2!=0):
    	r1[2]=not r1[2]
    	r1[1]=not r1[1]
    	r2[2]=not r2[2]
    if(b1%2!=0):
    	r2[0]=not r2[0]
    	r1[0]=not r1[0]
    	r2[1]=not r2[1]
    	r3[0]=not r3[0]
    if(b2%2!=0):
    	r2[1]=not r2[1]
    	r1[1]=not r1[1]
    	r2[0]=not r2[0]
    	r2[2]=not r2[2]
    	r3[1]=not r3[1]
    if(b3%2!=0):
    	r2[2]=not r2[2]
    	r1[2]=not r1[2]
    	r2[1]=not r2[1]
    	r3[2]=not r3[2]
    if(c1%2!=0):
    	r3[0]=not r3[0]
    	r2[0]=not r2[0]
    	r3[1]=not r3[1]
    if(c2%2!=0):
    	r3[1]=not r3[1]
    	r3[0]=not r3[0]
    	r2[1]=not r2[1]
    	r3[2]=not r3[2]
    if(c3%2!=0):
    	r3[2]=not r3[2]
    	r2[2]=not r2[2]
    	r3[1]=not r3[1]
    for i in range(0,3):
    	print(int(r1[i]),end='')
    print()
    for i in range(0,3):
    	print(int(r2[i]),end='')
    print()
    for i in range(0,3):
    	print(int(r3[i]),end='')
    print()