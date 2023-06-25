def program2177():
    x,y,z,t1,t2,t3=map(int,input().split())
    elevator=((abs(x-z)*t2)+2*t3)+((abs(x-y)*t2)+t3)
    stairs=abs(x-y)*t1
    
    if elevator<=stairs:
    	print('YES')
    else:
    	print('NO')