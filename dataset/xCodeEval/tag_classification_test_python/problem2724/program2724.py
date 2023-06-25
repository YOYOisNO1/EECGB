def program2724():
    
    s=input().split(':')
    a=int(s[0])
    b=int(s[1])
    
    s=input().split(':')
    x=int(s[0])
    y=int(s[1])
    
    b=b-y
    if b<0:
    	b=b+60
    	a-=1
    a=a-x
    if a<0:
    	a=a+24
    
    if a<10:
    	print('0',end="")
    print(a,end="")
    
    print(":",end="")
    if b<10:
    	print(0,end="")
    print(b,end="")