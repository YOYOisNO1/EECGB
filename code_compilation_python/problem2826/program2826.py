def program2826():
    x_1, y_2 = map(int, input().split())
    x_2, y_2 = map(int, input().split())
    
    if x_1 == x_2 or y_1 == y_2:
    	print((abs(x_2 - x_1) + abs(y_2 - y_1)) * 2 + 6)
    else:
    	print((abs(x_2 - x_1) + abs(y_2 - y_1) + 2) * 2)