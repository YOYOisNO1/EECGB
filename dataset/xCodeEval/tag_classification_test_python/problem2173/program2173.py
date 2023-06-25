def get_input_list():
    	return list(map(int, input().split()))
    
    x,y,z,t1,t2,t3 = get_input_list()
    a = (abs(z - x) + abs(y - x))* t2 + 3*t3
    b = abs(x-y)* t1
    if a>b:
    	print('NO')
    else:
    	print('YES')