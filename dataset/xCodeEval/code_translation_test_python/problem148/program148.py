def program148():
    x, y, z = map(int, input().split())
    a, b, c = map(int, input().split())
    if x <= a and y <= a+b-x and z <= a+b+c-y-x:
    	print('YES')
    else:
    	print("NO")